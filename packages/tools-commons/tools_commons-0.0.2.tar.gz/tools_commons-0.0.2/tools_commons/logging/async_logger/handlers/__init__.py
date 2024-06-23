import os
import time
import types
from collections.abc import Mapping
from typing import Optional, Tuple, Type

from aiologger.levels import LogLevel, get_level_name

ExceptionInfo = Tuple[Type[BaseException], BaseException, types.TracebackType]


class LogRecord:
    def __init__(
        self,
        name: str,
        level: LogLevel,
        pathname: str,
        lineno: int,
        msg,
        args: Optional[Tuple[Mapping]] = None,
        exc_info: Optional[ExceptionInfo] = None,
        func: Optional[str] = None,
        sinfo: Optional[str] = None,
        extra: Optional[dict] = None,
        **kwargs,
    ) -> None:
        created_at = time.time()
        self.name = name
        self.msg = msg
        self.args: Optional[Mapping]
        if args:
            if len(args) != 1 or not isinstance(args[0], Mapping):
                raise ValueError(
                    f"Invalid LogRecord args type: {type(args[0])}. "
                    f"Expected Mapping"
                )
            self.args = args[0]
        else:
            self.args = args
        self.levelname = get_level_name(level)
        self.levelno = level
        self.pathname = pathname
        try:
            self.filename = os.path.basename(pathname)
            self.module = os.path.splitext(self.filename)[0]
        except (TypeError, ValueError, AttributeError):
            self.filename = pathname
            self.module = "Unknown module"
        self.exc_info = exc_info
        self.exc_text: Optional[str] = None  # used to cache the traceback text
        self.stack_info = sinfo
        self.lineno = lineno
        self.funcName = func
        self.created = created_at
        self.msecs = (created_at - int(created_at)) * 1000
        self.process = os.getpid()
        self.asctime: Optional[str] = None
        self.message: Optional[str] = None
        self.extra = extra
        if not self.extra:
            self.extra = {}
        self.kwargs = kwargs

    def __str__(self):
        return (
            f"<{self.__class__.__name__}: {self.name}, {self.levelname}, "
            f'{self.pathname}, {self.lineno}, "{self.msg}">'
        )

    __repr__ = __str__

    def get_message(self):
        msg = str(self.msg)
        if self.args:
            msg = msg % self.args
        return msg


#replace default log-record class
import aiologger
aiologger.logger.LogRecord = LogRecord

from .slack_log_handler import AsyncSlackLogHandler
from .file_log_handler import FileLogHandler
from .stream_log_handler import AsyncStreamHandler
