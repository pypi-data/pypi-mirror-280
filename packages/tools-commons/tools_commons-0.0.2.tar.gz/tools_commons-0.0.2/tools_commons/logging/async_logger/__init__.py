import threading
import sys

from aiologger import Logger
from aiologger.formatters.base import Formatter
from aiologger.levels import LogLevel
from aiologger.filters import StdoutFilter
from .handlers import AsyncStreamHandler

_lock = threading.RLock()
root_logger = Logger(name="root")
formatter = Formatter('{"time":"%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}')
loggers = {"root": root_logger}


def critical(msg, *args, **kwargs):
    return root_logger.critical(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    return root_logger.error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    return root_logger.warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    return root_logger.info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    return root_logger.debug(msg, *args, **kwargs)


def getLogger(name: str, *args, **kwargs):
    if name is None:
        return root_logger

    if name not in loggers:
        _lock.acquire()
        try:
            if name not in loggers:
                _logger = Logger(name=name, *args, **kwargs)
                loggers[name] = _logger
        finally:
            _lock.release()

    return loggers[name]


def add_default_handlers(_logger: Logger):
    _logger.add_handler(AsyncStreamHandler(stream=sys.stdout, level=LogLevel.DEBUG, formatter=formatter, filter=StdoutFilter()))
    _logger.add_handler(AsyncStreamHandler(stream=sys.stderr, level=LogLevel.WARNING, formatter=formatter))


add_default_handlers(root_logger)
