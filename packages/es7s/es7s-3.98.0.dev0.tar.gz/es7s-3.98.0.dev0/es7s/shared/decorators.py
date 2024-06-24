from __future__ import annotations

import typing as t
from contextlib import contextmanager
from functools import update_wrapper
from typing import overload

import pytermor as pt
from es7s_commons import DummyProgressBar, ProgressBar, InputMode

from .io_ import get_stdout
from .log import get_logger
from .termstate import ProxiedTerminalState
from .theme import ThemeColor

_F = t.TypeVar("_F", bound=t.Callable[..., t.Any])


@overload
def with_progress_bar(__origin: _F) -> _F:
    ...


@overload
def with_progress_bar(
    *,
    tasks_amount: int = None,
    task_num: int = None,
    task_label: str = None,
    steps_amount: int = None,
    step_num: int = None,
    print_step_num: bool = None,
) -> _F:
    ...


def with_progress_bar(__origin: _F = None, **kwargsdec) -> _F:
    """
    Requires TerminalState to work. If the command is not decorated with
    TerminalState, this decorator will wrap it up by itself.
    """

    def decorator(__origin: _F):
        def wrapper(*args, **kwargs):
            nonlocal __origin
            try:
                pbar = ProgressBar(
                    get_stdout().renderer,
                    get_stdout().io,
                    ThemeColor(),
                    **pt.filternv(kwargsdec or dict()),
                )
                get_stdout().enable_output_buffering(pbar)
                if termstate := kwargs.get("termstate", None):
                    termstate.hide_cursor()
                    termstate.setup_input(InputMode.DISABLED)
                else:
                    __origin = with_terminal_state(
                        no_cursor=True,
                        input_mode=InputMode.DISABLED,
                    )(__origin)
            except Exception as e:
                get_logger().warning(f"Failed to set up progress bar component: {e}")
                pbar = DummyProgressBar()
            try:
                # pbar MUST be present in decorated constructor args:
                __origin(pbar, *args, **kwargs)
            finally:
                pbar.close()
                get_stdout().disable_output_buffering()
            return __origin

        return update_wrapper(t.cast(_F, wrapper), __origin)

    if __origin is not None:
        return decorator(__origin)
    else:
        return decorator


@overload
def with_terminal_state(__origin: _F) -> _F:
    ...


@overload
def with_terminal_state(
    *,
    alt_buffer: bool = None,
    no_cursor: bool = None,
    input_mode: InputMode = None,
    tabs_interval: int = None,
    tabs_shift: int = None,
) -> _F:
    ...


def with_terminal_state(
    __origin: _F = None,
    *,
    alt_buffer: bool = None,
    no_cursor: bool = None,
    input_mode: InputMode = None,
    tabs_interval: int = None,
    tabs_shift: int = None,
) -> _F:
    def decorator(__origin: _F):
        def wrapper(*args, **kwargs):
            termstate = ProxiedTerminalState()

            if alt_buffer:
                termstate.enable_alt_screen_buffer()
            if no_cursor:
                termstate.hide_cursor()
            if input_mode:
                termstate.setup_input(input_mode)
            if tabs_interval:
                termstate.set_horiz_tabs(tabs_interval, tabs_shift)

            try:
                # termstate CAN be present in decorated constructor args:
                __origin(termstate=termstate, *args, **kwargs)
            finally:
                termstate.restore_state()
            return __origin

        return update_wrapper(t.cast(_F, wrapper), __origin)

    if __origin is not None:
        return decorator(__origin)
    else:
        return decorator


@contextmanager
def set_terminal_state(
    alt_buffer: bool = None,
    no_cursor: bool = None,
    input_mode: InputMode = None,
    tabs_interval: int = None,
    tabs_shift: int = None,
):
    termstate = ProxiedTerminalState()

    if alt_buffer:
        termstate.enable_alt_screen_buffer()
    if no_cursor:
        termstate.hide_cursor()
    if input_mode:
        termstate.setup_input(input_mode)
    if tabs_interval:
        termstate.set_horiz_tabs(tabs_interval, tabs_shift)

    try:
        yield termstate
    finally:
        termstate.restore_state()
