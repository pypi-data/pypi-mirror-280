import unittest
import threading
import asyncio
import os

from ..logging import async_logger as logging
from ..logging.async_logger.handlers import AsyncSlackLogHandler, FileLogHandler
from ..logging.async_logger import LogLevel
from ..logging.async_logger.log_loop import stop_thread


class LoggerTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
        stop_thread()

    def test_logger(self):
        logger_1 = logging.getLogger("root")
        logger_2 = logging.root_logger
        assert logger_1 == logger_2
        print(len(logger_2.handlers))
        assert len(logger_1.handlers) == 2

        logger_3 = logging.getLogger("test")
        assert logger_1 != logger_3
        print(len(logger_3.handlers))
        assert len(logger_3.handlers) == 0

    def test_logger_threadsafe(self):

        def _target():
            async def _log():
                await logging.info(f"In thread: {threading.get_ident()}")
                
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(_log())

        thread_1 = threading.Thread(target=_target)
        thread_2 = threading.Thread(target=_target)

        thread_1.start()
        thread_2.start()

        thread_1.join()
        thread_2.join()

    def test_file_handler(self):
        def _target(_logger):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            async def _log():
                await _logger.error(f"Hello there from thread: {threading.get_ident()}")

            loop.run_until_complete(_log())

        logger = logging.getLogger("file")
        handler = FileLogHandler(filename="logs_test.log", level=LogLevel.INFO)
        logger.add_handler(handler)

        thread_1 = threading.Thread(target=_target, args=(logger,))
        thread_2 = threading.Thread(target=_target, args=(logger,))

        thread_1.start()
        thread_2.start()

        thread_1.join()
        thread_2.join()

        assert os.path.exists("logs_test.log")

    def test_root_logger(self):
        async def _log():
            await logging.info("current timestamp: 162383965")
            await logging.info("current timestamp: 162383967")

        asyncio.get_event_loop().run_until_complete(_log())


if __name__ == "__main__":
    unittest.main(verbosity=2)
