# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import psutil

from es7s.shared import MemoryInfo, SocketTopic
from ._base import DataProvider


class MemoryProvider(DataProvider[MemoryInfo]):
    def __init__(self):
        super().__init__("memory", SocketTopic.MEMORY)

    def _collect(self) -> MemoryInfo:
        return MemoryInfo(
            phys_used=psutil.virtual_memory().used,
            phys_total=psutil.virtual_memory().total,
            swap_used=psutil.swap_memory().used,
            swap_total=psutil.swap_memory().total,
        )
