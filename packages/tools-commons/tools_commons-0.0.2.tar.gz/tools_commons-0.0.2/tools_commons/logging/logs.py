import logging
import sys
import time
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
from queue import Queue, Empty
from threading import Thread

stop_thread = False


class LogsManager:
    def __init__(self):
        self._global_logs_path = None

    def add_default_handler(self, out_stream=sys.stdout):
        """
        Setup a default handler with basic configuration for the logging.
        Handler will be added to root logger

        This is a StreamHandler and outputs on SYS.STDERR. Format and other fancy
        details are set to what is provided by the logger package

        handler level is set to NOT_SET which is level 0. It is expected of
        the root logger to set level requirements. This handler will not
        perform any filter of its own
        """
        handler = StreamHandler(stream=out_stream)

        formatter = logging.Formatter(
            '{"time":"%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}'
        )

        logging.root.handlers = []
        handler.setFormatter(formatter)
        logging.root.addHandler(handler)
        logging.root.setLevel(logging.INFO)

    def add_global_logs_handler(self):
        """
        This is the handler for writing logs to global_logs (Similar to app.py
        in intuition). Again we are not setting any level for this handler
        """
        handler = RotatingFileHandler(
            self._global_logs_path, maxBytes=(10485760 * 5), backupCount=7, mode="w"
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logging.root.addHandler(handler)
        logging.root.setLevel(logging.ERROR)

    def setup(self):
        """
        Setup logger to keep parity with intuition modules. We want to see
        logs in `global logs` as well as `docker logs` which requires 2 handlers.
        Intuition module accidentally creates a handler to STDERR while doing
        `import processor from Processor` in `visual_smartcare/app.py`
        :return:
        """
        self.add_default_handler()


def setup_logs():
    logsManager = LogsManager()
    logsManager.setup()


def get_log_level():
    return logging.getLevelName(logging.root.getEffectiveLevel())


def update_log_level(level):
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]

    def _update(new_level):
        logging.root.setLevel(new_level)
        for logger in loggers:
            logger.setLevel(new_level)

    prev_level = get_log_level()
    if level.lower() == "info":
        _update(logging.INFO)
    elif level.lower() == "error":
        _update(logging.ERROR)
    elif level.lower() == "debug":
        _update(logging.DEBUG)
    elif level.lower() == "warn":
        _update(logging.WARN)
    curr_level = get_log_level()
    logging.critical(
        "Updated Logger Level from {} to {}".format(prev_level, curr_level)
    )
    return curr_level


class DiffLog:
    def __init__(self, time, log):
        self.time = time
        self.log = log


class TimeDiffLogger:
    def __init__(self, log: str):
        self.log = log

    def __enter__(self):
        self.start = time.time() * 1000

    def __exit__(self, exc_type, exc_val, exc_tb):
        log = DiffLog(time.time() * 1000 - self.start, self.log)
        logging.info("{0} exiting, time taken : {1} ms".format(log.log, log.time))
