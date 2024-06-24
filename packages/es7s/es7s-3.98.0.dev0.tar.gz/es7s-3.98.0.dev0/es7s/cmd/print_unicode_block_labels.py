# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2024 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import io

import pytermor as pt
from click import pass_context
from es7s_commons import column

from ._base import _BaseAction
from es7s.shared import get_stdout, run_subprocess

import sys, re, unicodedata

from ..cli._base import Context

CHAR_LTR = "\u200e"
CHARB_LTR = CHAR_LTR.encode()


@pass_context
class action(_BaseAction):
    def __init__(self, ctx: Context, **kwargs):
        self._replacer = pt.EscSeqStringReplacer()
        self._run(ctx)

    def _run(self, ctx: Context):
        from holms.cli.entrypoint import LegendCommand
        from holms.shared.log import init_log

        __origin = sys.stdout
        sys.stdout = io.StringIO()
        init_log(0)
        ctx.invoke(LegendCommand)
        sys.stdout.seek(0)
        lines = sys.stdout.readlines()
        sys.stdout = __origin

        rows = []
        cols_w = []
        discard = True
        for line in lines:
            line = line.rstrip()
            if not (plain := self._replacer.apply(line).rstrip()):
                continue
            if discard and plain.startswith("UNICODE BLOCKS"):
                discard = False
                continue
            if not discard and plain.startswith("CODE POINT CATEGORY"):
                discard = True
            if discard:
                continue
            idx_strs = re.findall(R"(?i)[0-9A-F]+", plain)
            assert len(idx_strs) >= 2
            idx_min = int(idx_strs.pop(0), 16)
            idx_max = int(idx_strs.pop(0), 16)
            idx = idx_min

            def format_ucp_number(num: int) -> str:
                num_str = f"{num:04X}"
                return "U+"[: max(0, 6 - len(num_str))] + num_str

            row = None
            while idx <= idx_max:
                try:
                    cp = unicodedata.name(chr(idx))
                except Exception:
                    continue
                else:
                    if "LETTER A" in cp:
                        row = [
                            line,
                            format_ucp_number(idx) + "  " + cp,
                            CHAR_LTR + chr(idx) + CHAR_LTR,
                        ]
                        break
                finally:
                    idx += 1

            if idx >= idx_max:
                char = chr(idx_min)
                try:
                    cp = unicodedata.name(char)
                except ValueError:
                    cp = "(UNASSIGNED)"
                char = char.encode(errors="ignore").decode()
                row = [
                    line,
                    format_ucp_number(idx_min) + "  " + cp,
                    CHAR_LTR + char + CHAR_LTR,
                ]

            if not cols_w:
                cols_w = [0] * len(row) * 10  # fk my life
            for (cidx, cell) in enumerate(row):
                cols_w[cidx] = max(cols_w[cidx], len(self._replacer.apply(cell)))
            rows.append(row)

        data = [
            " │ ".join(
                [
                    cell + pt.pad(cols_w[cidx] - len(self._replacer.apply(cell)))
                    for (cidx, cell) in enumerate(row)
                ]
            )
            for row in rows
        ]
        tx, _ = column.columns(data)
        get_stdout().echo_rendered(tx)
