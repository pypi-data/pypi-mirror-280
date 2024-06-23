import asyncio
import sys
from asyncio import AbstractEventLoop, StreamWriter
from typing import Union, Optional

from aiologger.filters import Filter
from aiologger.formatters.base import Formatter
from aiologger.handlers.base import Handler
from aiologger.protocols import AiologgerProtocol
from aiologger.levels import LogLevel

from ..log_loop import run_coro
from ..handlers import LogRecord


class AsyncStreamHandler(Handler):
    terminator = "\n"

    def __init__(
        self,
        stream=None,
        level: Union[str, int, LogLevel] = LogLevel.NOTSET,
        formatter: Formatter = None,
        filter: Filter = None,
    ) -> None:
        super().__init__()
        if stream is None:
            stream = sys.stderr
        self.stream = stream
        self.level = level
        if formatter is not None:
            self.formatter: Formatter = formatter
        if filter:
            self.add_filter(filter)
        self.protocol_class = AiologgerProtocol
        self._lock: Optional[asyncio.Lock] = None
        self._writer: Optional[StreamWriter] = None

    @property
    def initialized(self):
        return self._writer is not None

    async def _get_writer(self) -> StreamWriter:
        if not self.initialized:
            if not self._lock:
                self._lock = asyncio.Lock()
            async with self._lock:
                if not self.initialized:
                    loop = asyncio.get_event_loop()
                    transport, protocol = await loop.connect_write_pipe(self.protocol_class, self.stream)
                    self._writer = StreamWriter(transport=transport, protocol=protocol, reader=None, loop=loop)
        return self._writer

    async def handle(self, record: LogRecord) -> bool:
        """
        Conditionally emit the specified logging record.
        Emission depends on filters which may have been added to the handler.
        """
        rv = self.filter(record)
        if rv:
            await self.emit(record)
        return rv

    async def flush(self):
        if self.initialized:
            await run_coro(self._writer.drain())

    async def emit(self, record: LogRecord):
        """
        Actually log the specified logging record to the stream.
        """
        try:
            await run_coro(self._emit(record))
        except Exception as exc:
            await self.handle_error(record, exc)

    async def _emit(self, record: LogRecord):
        self._writer = await self._get_writer()
        msg = self.formatter.format(record) + self.terminator
        self._writer.write(msg.encode())
        await self._writer.drain()

    async def close(self):
        """
        Tidy up any resources used by the handler.

        This version removes the handler from an internal map of handlers,
        should ensure that this gets called from overridden close()
        methods.
        """
        if self.initialized:
            await run_coro(self.flush())
            self._writer.close()
