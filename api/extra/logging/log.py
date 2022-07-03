from datetime import datetime
from enum import Enum


class Log:
    def __init__(self, lvl, msg, ref = None, err = None, time = None):
        super().__init__()
        self._timestamp = datetime.now() if time is None else time
        self._lvl = lvl
        self._msg = msg
        self._ref = ref
        self._err = err
        self._logstr = self._get_timeless_log()

    def __str__(self):
        result = self._get_timestamp_format()
        result = result + self._get_timeless_log()
        return result

    def _get_timestamp_format(self):
        return '[' + str(self._timestamp) + ']: '

    def _get_timeless_log(self):
        result = '[' + str(self._lvl) + '] - '
        result = result + str(self._msg)
        if self._ref is not None:
            result = result + "\n\t"
            result = result + str(self._ref)
        if self._err is not None:
            if isinstance(self._err, Exception):
                result = result + "\n\t"
                result = result + str(self._err.args[0])
        return result

class LogLevel(Enum):
    ERROR = 0
    WARN = 1
    DEBUG = 2
    SUCCESS = 3