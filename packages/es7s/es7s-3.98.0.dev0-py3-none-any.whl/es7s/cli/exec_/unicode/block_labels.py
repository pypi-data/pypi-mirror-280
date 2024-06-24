# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2024 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from ..._decorators import cli_command, catch_and_log_and_exit


@cli_command(__file__, "display unicode category labels")
@catch_and_log_and_exit
class invoker:
    """
    Display unicode category labels.
    """

    def __init__(self, **kwargs):
        from es7s.cmd.print_unicode_block_labels import action

        action(**kwargs)
