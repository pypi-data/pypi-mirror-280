"""
Asynchronous thread-safe log handler to store logs in a file.
"""
import asyncio
import os
import aiofiles
from typing import Union, Dict, Optional
from asyncio import AbstractEventLoop
from aiofiles.threadpool import AsyncTextIOWrapper

from aiologger.handlers.base import Handler
from aiologger.filters import Filter
from aiologger.formatters.base import Formatter
from ...async_logger import LogLevel
from ..log_loop import run_coro
from ..handlers import LogRecord


class FileLogHandler(Handler):
    terminator = "\n"

    def __init__(
        self,
        filename: str,
        encoding: str = None,
        level: Union[str, int, LogLevel] = LogLevel.NOTSET,
        formatter: Formatter = None,
        filter: Filter = None,
    ) -> None:
        super().__init__()
        filename = os.fspath(filename)
        self.level = level
        self.absolute_file_path = os.path.abspath(filename)
        self.encoding = encoding
        self._writer: Optional[AsyncTextIOWrapper] = None
        self._lock: Optional[asyncio.Lock] = None
        if formatter is not None:
            self.formatter: Formatter = formatter
        if filter:
            self.add_filter(filter)

    @property
    def initialized(self):
        return self._writer is not None

    async def get_writer(self) -> AsyncTextIOWrapper:
        """
        Open the current base file with the (original) mode and encoding.
        """
        if not self.initialized:
            if not self._lock:
                self._lock = asyncio.Lock()
            async with self._lock:
                if not self.initialized:
                    self._writer = await aiofiles.open(file=self.absolute_file_path, mode="a", encoding=self.encoding)
        return self._writer

    async def flush(self):
        if self.initialized:
            await run_coro(self._writer.flush())

    async def close(self):
        if self.initialized:
            await run_coro(self._writer.close())
        self._writer = None
        self._lock = None

    async def emit(self, record: LogRecord):
        try:
            await run_coro(self._emit(record))
        except Exception as exc:
            await self.handle_error(record, exc)

    async def _emit(self, record: LogRecord):
        _msg = self.formatter.format(record)
        _writer = await self.get_writer()
        await _writer.write(_msg + self.terminator)
        await _writer.flush()