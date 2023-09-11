from typing import Optional

from ._execution_log import ExecutionLog
from ._execution_log_entry import ExecutionLogEntry
from ._monitored import Monitored


class ExecutionContext:
    _executionLog: ExecutionLog
    _entry: ExecutionLogEntry

    def __init__(self, execution_log: Optional[ExecutionLog] = None, path: str = ""):
        self._executionLog = execution_log or ExecutionLog()
        self._entry = self._executionLog.new_entry(path)

    def _new_path(self, name: str):
        return name if self._entry.source == "" else f"{self._entry.source}/{name}"

    def new_from_name(self, name: str):
        return ExecutionContext(self._executionLog, self._new_path(name))

    def new_for(self, monitored: Monitored) -> "ExecutionContext":
        return ExecutionContext(self._executionLog, self._new_path(monitored.name))

    @property
    def entry(self) -> ExecutionLogEntry:
        return self._entry