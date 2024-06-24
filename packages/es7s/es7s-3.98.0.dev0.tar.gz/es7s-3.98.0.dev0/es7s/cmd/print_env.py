# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023-2024 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from __future__ import annotations

import re
import typing as t
from dataclasses import dataclass
from io import StringIO
from math import ceil
from typing import List, Dict

import pytermor as pt
from es7s_commons import re_unescape

from es7s.shared import FrozenStyle, get_stdout, Styles as BaseStyles, ENV_PATH, run_subprocess
from es7s.shared.enum import MarginMode, QuoteMode
from ._adaptive_input import _AdaptiveInputAction
from ._base import _BaseAction


class action(_AdaptiveInputAction, _BaseAction):
    def __init__(
        self,
        margin: MarginMode,
        quote: QuoteMode,
        no_prefix: bool,
        keep_sgr: bool,
        literal: bool,
        filter: t.Iterable[str],
        **kwargs,
    ):
        super().__init__(**kwargs)

        self._margin = margin
        self._quote = quote
        self._no_prefix = no_prefix
        self._keep_sgr = keep_sgr
        self._and = kwargs.get("and")

        if literal:
            self._filters = [*filter]
        else:
            try:
                flags = re.IGNORECASE if all(f.islower() for f in filter) else 0
                self._filters = [re.compile(re_unescape(f), flags=flags) for f in filter]
            except re.error as e:
                raise RuntimeError(f"Failed to compile filter regular expression: {e}")

        self._run()

    def _get_default_file(self) -> StringIO:
        cp = run_subprocess(ENV_PATH)
        return StringIO(cp.stdout)

    def _run(self):
        evars = self._parse(self._input_lines)
        if len(evars.keys()) == 0:
            return

        stdout = get_stdout()
        for result in self._filter(self._format(evars)):
            stdout.echo_rendered(result.result_key, nl=False)
            if stdout.sgr_allowed:
                stdout.echo_rendered(result.val_str, result.val_fmt, nl=False)
            else:
                if self._keep_sgr:
                    stdout.echo_direct(result.val_str, nl=False)
                else:
                    stdout.echo(result.val_str, nl=False)
            stdout.echo(pt.SeqIndex.RESET)
            stdout.echo()

    def _parse(self, inp_lines: List[str]) -> Dict[str, EnvVar]:
        evars = dict()
        for line in inp_lines:
            if (
                "=" not in line
                or line.startswith(";")
                or not re.match(r"^\s*[A-Za-z0-9_. ]+=", line)
            ):
                continue
            key, val_str = (p.strip() for p in line.split("=", 1))

            is_active = not key.startswith("#")
            key = key.lstrip("#")

            if key not in evars.keys():
                evars[key] = EnvVar(key)
            evars[key].add(EnvVarValue(val_str, is_active))

        return evars

    def _filter(self, result: t.Iterable[FormatResult]) -> t.Iterable[FormatResult]:
        if not self._filters:
            return result

        def _fn(fr: FormatResult) -> bool:
            aggregator = all if self._and else any
            return aggregator(_match(f, fr) for f in self._filters)

        def _match(f: str | re.Pattern, fr: FormatResult) -> bool:
            if isinstance(f, str):
                return f in fr.origin_key
            return bool(f.search(fr.origin_key))

        return filter(_fn, result)

    def _format(self, evars: Dict[str, EnvVar]) -> t.Iterable[FormatResult]:
        max_key_len = None

        if self._margin in [MarginMode.FULL, MarginMode.HALF]:
            max_key_len = max(len(k) for k in evars.keys())
            if self._margin is MarginMode.HALF:
                max_key_len = ceil(max_key_len / 2)

        for idx, key in enumerate(sorted(evars.keys(), key=lambda k: k)):
            yield from self._format_val(evars[key], idx, key, max_key_len)

    def _format_val(
        self,
        vals: EnvVar,
        idx: int,
        key: str,
        max_key_len: int,
    ) -> t.Iterable[FormatResult]:
        for local_idx, val in enumerate(vals.vals_active + vals.vals_idle):
            val_str = val.val_str
            result_key = pt.Text()

            is_even = (idx + local_idx) % 2 == 0
            is_duplicate = local_idx < len(vals.vals_active) - 1 and val.is_active

            key_prefix = pt.Fragment(" ")
            fmt_for_key = pt.NOOP_STYLE
            fmt_for_equals = pt.NOOP_STYLE
            fmt_for_val = pt.NOOP_STYLE

            if get_stdout().sgr_allowed:
                fmt_even = [] if is_even else [_Styles.EVEN_OW]
                fmt_for_equals = pt.merge_styles(_Styles.EQUALS, overwrites=fmt_even)

                if is_duplicate:
                    key_prefix = pt.Fragment("!", _Styles.DUPLICATE_PREFIX)
                    fmt_for_key = pt.merge_styles(_Styles.DUPLICATE_KEY, overwrites=fmt_even)
                    fmt_for_val = pt.merge_styles(_Styles.DUPLICATE_VALUE, overwrites=fmt_even)
                elif not val.is_active or len(val_str) == 0:
                    fmt_for_key = pt.merge_styles(_Styles.EMPTY_KEY, overwrites=fmt_even)
                    fmt_for_val = _Styles.EMPTY_VALUE
                elif is_even:
                    fmt_for_key = _Styles.ACTIVE_EVEN_KEY
                    fmt_for_val = _Styles.ACTIVE_EVEN_VALUE
                else:
                    fmt_for_key = _Styles.ACTIVE_ODD_KEY
                    fmt_for_val = _Styles.ACTIVE_ODD_VALUE

            if not self._no_prefix:
                result_key += key_prefix
            result_key += pt.Fragment(key, fmt_for_key)

            if max_key_len:
                if pad_len := max(0, max_key_len - len(key)):
                    result_key += pt.Fragment(" " * pad_len)
            result_key += pt.Fragment("=", fmt_for_equals)

            if len(val_str) > 0:
                quote_always = self._quote is QuoteMode.ALWAYS
                quote_auto = self._quote is QuoteMode.AUTO
                val_has_spaces = re.search(r"\s", val_str)
                val_has_escapes = re.search(r"\x1b", val_str)
                if quote_always or (quote_auto and (val_has_spaces or val_has_escapes)):
                    val_str = f'"{val_str}"'
                if val_has_escapes:
                    fmt_for_val = pt.NOOP_STYLE

            yield FormatResult(key, result_key, val_str, fmt_for_val)


class _Styles(BaseStyles):
    EVEN_OW = FrozenStyle(dim=True)
    EQUALS = FrozenStyle(fg=pt.cv.GRAY)

    EMPTY_KEY = FrozenStyle(fg=pt.cv.WHITE)
    EMPTY_VALUE = pt.NOOP_STYLE

    ACTIVE_ODD_KEY = FrozenStyle(fg=pt.cv.GREEN)
    ACTIVE_ODD_VALUE = FrozenStyle(fg=pt.cv.BLUE)
    ACTIVE_EVEN_KEY = FrozenStyle(fg=pt.cv.HI_GREEN)
    ACTIVE_EVEN_VALUE = FrozenStyle(fg=pt.cv.HI_BLUE)

    DUPLICATE_PREFIX = FrozenStyle(bg=pt.cv.RED, bold=True)
    DUPLICATE_KEY = FrozenStyle(fg=pt.cv.RED, crosslined=True)
    DUPLICATE_VALUE = FrozenStyle(fg=pt.cv.GRAY, crosslined=True)


@dataclass
class FormatResult:
    origin_key: str
    result_key: pt.Text
    val_str: str
    val_fmt: pt.Style


class EnvVar:
    def __init__(self, key: str):
        self.key: str = key
        self.vals_active: List[EnvVarValue] = []
        self.vals_idle: List[EnvVarValue] = []

    def add(self, val: EnvVarValue):
        vals = self.vals_active if val.is_active else self.vals_idle
        vals.append(val)


class EnvVarValue:
    def __init__(self, val_raw: str, is_active: bool):
        self.val_str: str = val_raw.strip()
        self.comment: str | None = None
        self.is_active: bool = is_active

        self._sanitize()

    def _sanitize(self):
        # comments start with '#', but if it's quoted, it will
        # be not a comment anymore, but a part of the value
        try:
            hash_pos = self.val_str.rindex("#")
        except ValueError:  # there are no hashes in value
            return

        if self.val_str.startswith(('"', "'")):
            try:
                last_matching_quote_pos = self.val_str.rindex(self.val_str[0])
            except ValueError:  # malformed quotes?
                pass  # consider it comment anyway
            else:
                if hash_pos < last_matching_quote_pos:  # part of the value
                    return

        self.val_str = self.val_str[:hash_pos].rstrip()
        self.comment = self.val_str[hash_pos:]


# original G1 version:
# -----------------------------------------------------------------------------
# _e=$'\e'
# env | \
#   sort | \
#   sed -E \
#       -e "s/(^[^=]+)(=)$/$_gy\1$_f/" \
#       -e "s/(^[^=$_e]+)(=)(.+)$/$_gn\1$_f\t\"$_be\3$_f\"/" \
#       -e "1~2s/^($_e\[)3/\19/" \
#       -e "1~2s/(\"$_e\[)3/\19/" \
#       -e "s/\"(\S+)\"$/\1/"  | \
#   column -t -s$'\t' | \
#   less -SR
