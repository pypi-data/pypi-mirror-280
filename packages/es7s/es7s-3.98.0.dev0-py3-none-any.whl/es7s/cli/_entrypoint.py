# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2021-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from __future__ import annotations

import copy
import datetime
import os
import re
import signal
import sys

import click
import pytermor as pt
from es7s_commons import format_path, PKG_VERSION, PKG_UPDATED

from es7s import APP_NAME, APP_UPDATED, APP_VERBOSITY, APP_VERSION
from es7s.shared import (
    UserConfigParams,
    IoParams,
    LoggerParams,
    destroy_io,
    destroy_logger,
    get_logger,
    get_stderr,
    get_stdout,
    init_config,
    init_io,
    init_logger,
    uconfig,
    get_signal_desc,
)
from es7s.shared import exit_gracefully
from ._base import (
    CliGroup,
    Context,
    HelpFormatter,
)
from ._base_opts_params import CommandOption, HelpPart
from ._decorators import catch_and_log_and_exit, cli_group, cli_option, cli_pass_context
from ._logo import LogoFormatter
from .autodiscover import AutoDiscover


def invoker():
    os.environ.update({"ES7S_DOMAIN": "CLI"})
    try:
        init_cli()
        callback()
    except SystemExit:
        destroy_cli()
        raise


def init_cli():
    pre_filtered_args = copy.copy(sys.argv)
    logger_params, io_params, ucp_params, spec_args = _filter_common_args(sys.argv)
    sys.argv = spec_args

    logger = init_logger(params=logger_params)
    _, _ = init_io(io_params)
    init_config(ucp_params)

    post_filtered_args = sys.argv

    logger.log_init_params(
        ("Executable:", format_path(sys.executable)),
        ("Entrypoint:", format_path(__file__)),
    )
    if hasattr(sys, "orig_argv"):
        logger.log_init_params(("Original app args:", getattr(sys, "orig_argv")))
    logger.log_init_params(
        ("Pre-init app args:", pre_filtered_args),
        ("Post-init app args:", post_filtered_args),
        ("Log configuration:", logger_params),
        ("Logger setup:", {"handlers": logger.handlers}),
        ("IO configuration:", io_params),
        ("Stdout proxy setup:", get_stdout().as_dict()),
        ("Stderr proxy setup:", get_stderr().as_dict()),
    )
    logger.addaudithook()

    [signal.signal(s, c) for s, c in _SIG_HANDLERS]
    signal.setitimer(signal.ITIMER_REAL, 1.0, 1.0)


def destroy_cli():
    signal.setitimer(signal.ITIMER_REAL, 0.0)
    [signal.signal(s, signal.SIG_DFL) for s, _ in _SIG_HANDLERS]
    # if stdout := get_stdout(False):
    #     stdout.echo('')
    destroy_io()
    destroy_logger()


def _audit_event(ev: str, *args):
    match ev.split(".")[0]:
        case "os" | "subprocess" | "shutil" | "tempfile" | "importlib":
            if logger := get_logger(require=False):
                logger.log_audit_event(ev, *args)
            return


def _exit(signal_code: int, *args):
    _log_signal(signal_code)
    exit_gracefully(signal_code)


def _clock_tick(signal_code: int, *args):
    _log_signal(signal_code)


_SIG_HANDLERS = [
    (signal.SIGINT, _exit),
    (signal.SIGTERM, _exit),
    (signal.SIGALRM, _clock_tick),
]


def _log_signal(signal_code: int, frame=None):
    get_logger(require=False).debug("Received " + get_signal_desc(signal_code))


class EntrypointCliGroup(CliGroup):
    recursive_command_list = False
    command_list_header = "Command groups"

    def _make_command_name(self, orig_name: str, **kwargs) -> str:
        return APP_NAME

    def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None:
        if ctx.failed:
            super().format_usage(ctx, formatter)
            return
        formatter.buffer.append(LogoFormatter.render())
        super().format_usage(ctx, formatter)


class VersionOption(CommandOption):
    SPACE_SQUASHER = pt.StringReplacer(r"(\s)\s+", r"\1")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("count", True)
        kwargs.setdefault("expose_value", False)
        kwargs.setdefault("is_eager", True)
        kwargs["callback"] = self.callback
        super().__init__(*args, **kwargs)

    def callback(self, ctx: click.Context, param: click.Parameter, value: int):
        if not value or ctx.resilient_parsing:
            return
        stdout = get_stdout()
        vfmt = lambda s: pt.Fragment(s, "green")

        def ufmt(s):
            try:
                dt = datetime.datetime.strptime(s.partition(" ")[0], "%Y-%m-%d")
                s = dt.strftime("%b %Y")
            except ValueError:
                pass
            return pt.Fragment(s, "gray")

        stdout.echo(f"{APP_NAME:>12s}  {vfmt(APP_VERSION):<14s}  {ufmt(APP_UPDATED)}")
        stdout.echo(f"{'es7s.commons':>12s}  {vfmt(PKG_VERSION):<14s}  {ufmt(PKG_UPDATED)}")
        stdout.echo(f"{'pytermor':>12s}  {vfmt(pt.__version__):<14s}  {ufmt(pt.__updated__)}")
        self._echo_python_version(vfmt, ufmt)
        self._echo_gi_version()

        if value > 1:

            def _echo_path(label: str, path: str):
                stdout.echo_rendered(
                    pt.Composite(
                        pt.Text(label + ":", width=17),
                        format_path(path, color=True, repr=False),
                    )
                )

            stdout.echo()
            _echo_path("Executable", sys.executable)
            _echo_path("Entrypoint", __file__)
            _echo_path("Local config", uconfig.get_local_filepath())
            _echo_path("Default config", uconfig.get_default_filepath())

        ctx.exit()

    def _echo_python_version(self, vfmt, ufmt):
        get_stdout().echo(
            re.sub(
                r"^(\S+) *\(\S+, *(\S+) *\S+( *\S+),.+?\) *.+$",
                lambda m: "  ".join(
                    [
                        f'{"python":>12s}',
                        f"{vfmt(m[1]):<14s}",
                        f"{ufmt(self.SPACE_SQUASHER.apply((m[2]+m[3]).strip())):s}",
                    ]
                ),
                sys.version,
            )
        )

    def _echo_gi_version(self):
        try:
            import gi
        except ImportError:
            return
        else:
            gi_v = ".".join(str(p) for p in gi.version_info)
            get_stdout().echo(f"{'[gtk]':>12s}  " + pt.render(gi_v, "blue"))


@cli_group(
    name=__file__,
    cls=EntrypointCliGroup,
    epilog=HelpPart(
        "Run 'es7s --version' (or '-V') to get the application version, or '-VV' to also include path info.",
        group="run",
    ),
)
@cli_option("--version", "-V", cls=VersionOption, help="Show the version and exit.")
@cli_pass_context
@catch_and_log_and_exit
def callback(ctx: click.Context, *args, **kwargs):
    """
    Entrypoint of es7s system CLI.
    """
    # triggers before subcommand invocation


def _filter_common_args(
    args: list[str],
) -> tuple[LoggerParams, IoParams, UserConfigParams, list[str]]:
    """
    Process common options manually because we want to allow specifying
    them everywhere: 'es7s -v print colors' and  'es7s print colors -v'
    should be equivalent, but this logic should not be applied to command-specific
    options, only to the common ones.
    """
    filtered = []
    lp = LoggerParams()
    iop = IoParams()
    ucp = UserConfigParams()

    if APP_VERBOSITY:
        lp.verbosity = APP_VERBOSITY

    def process_arg(arg: str):
        is_lopt = arg.startswith("--")
        is_shopt = arg.startswith("-") and not is_lopt

        if is_lopt or (is_shopt and len(arg) == 2):
            match arg:
                case "--verbose" | "-v":
                    lp.verbosity += 1
                case "--trace":
                    lp.verbosity += 3
                case "--quiet" | "-Q":
                    lp.quiet = True
                case "--tmux":
                    iop.tmux = True
                case "--color" | "-c":
                    iop.color = True
                case "--no-color" | "-C":
                    iop.color = False
                case "--default":
                    ucp.default = True
                case _:
                    filtered.append(arg)
        elif is_shopt:
            for c in arg.lstrip("-"):
                process_arg("-" + c)
        else:
            filtered.append(arg)

    while (len(args)) and (a := args.pop(0)):
        if a == "-":
            filtered.append(a)
            continue
        if a == "--":
            filtered += ["--"] + args
            break
        process_arg(a)

    return lp, iop, ucp, filtered
