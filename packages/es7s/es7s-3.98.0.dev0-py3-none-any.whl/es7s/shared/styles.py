# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import typing as t

import pytermor as pt
from pytermor import Style, CDT


class FrozenStyle(pt.Style):
    def __init__(
        self,
        fallback: Style = None,
        fg: CDT | pt.RenderColor = None,
        bg: CDT | pt.RenderColor = None,
        *,
        bold: bool = None,
        dim: bool = None,
        italic: bool = None,
        underlined: bool = None,
        overlined: bool = None,
        crosslined: bool = None,
        double_underlined: bool = None,
        curly_underlined: bool = None,
        underline_color: pt.CXT = None,
        inversed: bool = None,
        blink: bool = None,
        class_name: str = None,
    ):
        super().__init__(
            fallback,
            fg,
            bg,
            frozen=True,
            bold=bold,
            dim=dim,
            italic=italic,
            underlined=underlined,
            overlined=overlined,
            crosslined=crosslined,
            double_underlined=double_underlined,
            curly_underlined=curly_underlined,
            underline_color=underline_color,
            inversed=inversed,
            blink=blink,
            class_name=class_name,
        )


class Styles(pt.Styles):
    VALUE_OVERFLOW_CHAR = "⍙"  # ô

    TEXT_DISABLED = FrozenStyle(fg=pt.cv.GRAY_23)
    TEXT_LABEL = FrozenStyle(fg=pt.cv.GRAY_35)
    TEXT_DEFAULT = FrozenStyle(fg=pt.cv.GRAY_62)

    MSG_SUCCESS = FrozenStyle(fg=pt.cv.GREEN)
    MSG_SUCCESS_DETAILS = FrozenStyle(fg=pt.cv.GREEN)
    MSG_SUCCESS_LABEL = FrozenStyle(fg=pt.cv.HI_GREEN)
    MSG_FAILURE = FrozenStyle(fg=pt.cv.HI_RED)
    MSG_FAILURE_DETAILS = FrozenStyle(fg=pt.cv.RED)
    MSG_FAILURE_LABEL = FrozenStyle(fg=pt.cv.HI_WHITE, bg=pt.cv.DARK_RED, bold=True)

    SBAR_BG = pt.NOOP_COLOR

    VALUE_LBL_5 = TEXT_LABEL
    VALUE_UNIT_4 = TEXT_LABEL
    VALUE_FRAC_3 = FrozenStyle(fg=pt.cv.GRAY_50)
    VALUE_PRIM_2 = TEXT_DEFAULT
    VALUE_PRIM_1 = FrozenStyle(fg=pt.cv.GRAY_70, bold=True)

    TEXT_ACCENT = FrozenStyle(fg=pt.cv.GRAY_85)
    TEXT_SUBTITLE = FrozenStyle(fg=pt.cv.GRAY_93, bold=True)
    TEXT_TITLE = FrozenStyle(fg=pt.cv.HI_WHITE, bold=True, underlined=True)
    TEXT_UPDATED = FrozenStyle(fg=pt.cv.HI_GREEN, bold=True)
    TEXT_VALUE_OVERFLOW_CHAR = FrozenStyle(fg=pt.cv.DARK_ORANGE, bold=True, blink=True)
    TEXT_VALUE_OVERFLOW_LABEL = FrozenStyle(fg=pt.cv.YELLOW, bold=True)

    BORDER_DEFAULT = FrozenStyle(fg=pt.cv.GRAY_30)
    FILL_DEFAULT = FrozenStyle(fg=pt.cv.GRAY_46)

    STDERR_DEBUG = FrozenStyle(fg=pt.cv.MEDIUM_PURPLE_7)
    STDERR_AEVNT = FrozenStyle(fg=pt.cv.PLUM_4)
    STDERR_TRACE = FrozenStyle(fg=pt.cv.PALE_TURQUOISE_4)

    # PBAR_BG = pt.Style(bg=pt.cv.GRAY_3)
    PBAR_DEFAULT = FrozenStyle(TEXT_DEFAULT, bg=pt.cv.GRAY_19)
    PBAR_ALERT_1 = FrozenStyle(fg=pt.cv.GRAY_7, bg=pt.cv.ORANGE_3)
    PBAR_ALERT_2 = FrozenStyle(PBAR_ALERT_1, bg=pt.cv.DARK_GOLDENROD)
    PBAR_ALERT_3 = FrozenStyle(PBAR_ALERT_1, bg=pt.cv.ORANGE_2)
    PBAR_ALERT_4 = FrozenStyle(PBAR_ALERT_1, bg=pt.cv.DARK_ORANGE)
    PBAR_ALERT_5 = FrozenStyle(PBAR_ALERT_1, bg=pt.cv.ORANGE_RED_1)
    PBAR_ALERT_6 = FrozenStyle(PBAR_ALERT_1, bg=pt.cv.RED_3)
    PBAR_ALERT_7 = pt.Styles.CRITICAL_ACCENT

    DEBUG = FrozenStyle(fg=0x8163A2, bg=0x000444, underlined=True, overlined=True, blink=False)
    DEBUG_SEP_INT = FrozenStyle(fg=0x7280E2)
    DEBUG_SEP_EXT = FrozenStyle(fg=0x7E59A9)


class GrobocopStyles(Styles):
    def __init__(self):
        self.DEFAULT = self.TEXT_SUBTITLE
        self.CC = pt.Style(fg=pt.cv.HI_RED)
        self.WS = pt.Style(fg=pt.cv.CYAN)
        self.UNASSIGNED = self.TEXT_LABEL
        self.ERROR = pt.Style(fg=pt.cv.HI_YELLOW, bg=pt.cv.DARK_RED)
        self.OVERRIDE = pt.Style(fg=pt.cv.YELLOW)
        self.MULTIBYTE = pt.Style(fg=pt.cv.DEEP_SKY_BLUE_1)
        self.BG = pt.Style(bg=pt.cv.NAVY_BLUE)
        self.SUB_BG = pt.Style(bg=pt.cv.DARK_BLUE, bold=True).autopick_fg()
        self.SUBTITLE = pt.Style(self.BG, bold=True, fg="gray-89")
        self.UNDEFINED = pt.Style(self.BG, fg=pt.cv.DARK_BLUE)
        self.BG_TOP = pt.Style(self.UNDEFINED, overlined=True)
        self.AXIS = pt.Style(self.BG, fg=pt.cvr.AIR_SUPERIORITY_BLUE)


class VarTableStyles(Styles):
    _instance: t.Optional["VarTableStyles"] = None

    @classmethod
    def instantiate(cls):
        cls._instance = VarTableStyles()

    def __init__(self):
        self.VARIABLE_KEY_FMT = FrozenStyle(fg=pt.cvr.AIR_SUPERIORITY_BLUE, bold=True)
        self.VARIABLE_PUNCT_FMT = FrozenStyle(fg=pt.cvr.ATOMIC_TANGERINE)
        self.VARIABLES_FMT = {
            str: FrozenStyle(fg=pt.cvr.YOUNG_BAMBOO),
            int: FrozenStyle(fg=pt.cvr.CELESTIAL_BLUE),
            float: FrozenStyle(fg=pt.cvr.CELESTIAL_BLUE),
            bool: FrozenStyle(fg=pt.cvr.ICATHIAN_YELLOW),
        }

    def format_variable(self, v: any) -> pt.Fragment:
        if type(vc := v) in self.VARIABLES_FMT.keys():
            if isinstance(v, float):
                vc = f"{v:.2f}"
            elif isinstance(v, bool) or isinstance(v, int):
                vc = str(v)
            return pt.Fragment(vc, self.VARIABLES_FMT.get(type(v)))
        return self.format_variable(str(v))


def format_variable(v: any) -> pt.Fragment:
    if not VarTableStyles._instance:
        VarTableStyles.instantiate()
    return VarTableStyles._instance.format_variable(v)


def format_value_overflow(max_len=1) -> pt.Composite:
    if max_len == 0:
        return pt.Composite()

    char_fg = pt.Fragment(Styles.VALUE_OVERFLOW_CHAR, Styles.TEXT_VALUE_OVERFLOW_CHAR)
    if max_len == 1:
        return pt.Composite(char_fg)

    max_len -= 1
    label_fg = pt.Fragment(
        "OVERFLOW"[:max_len].ljust(max_len, "-"), Styles.TEXT_VALUE_OVERFLOW_LABEL
    )
    return pt.Composite(char_fg, label_fg)
