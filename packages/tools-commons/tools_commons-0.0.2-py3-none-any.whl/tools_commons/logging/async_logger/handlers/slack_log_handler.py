"""
Asynchronous thread-safe log handler to send logs to slack channel.
"""
import asyncio
import aiohttp
from typing import Union, Dict, Optional
from asyncio import AbstractEventLoop
from aiologger.filters import Filter
from aiologger.formatters.base import Formatter
from aiologger.handlers.base import Handler
from ...async_logger import LogLevel
from ..log_loop import run_coro
from ..handlers import LogRecord


_DEFAULT_CHANNEL_NAME = "#scheduler-job-alerts"


class AsyncSlackLogHandler(Handler):
    def __init__(
        self,
        api_token,
        level: Union[str, int, LogLevel] = LogLevel.NOTSET,
        formatter: Formatter = None,
        filter: Filter = None,
        default_channel=_DEFAULT_CHANNEL_NAME
    ) -> None:
        super().__init__()
        assert api_token
        self.api_token = api_token
        self.level = level
        self._session: Optional[aiohttp.ClientSession] = None
        self.default_channel = default_channel
        if formatter is not None:
            self.formatter: Formatter = formatter
        if filter:
            self.add_filter(filter)

    @property
    def initialized(self):
        return self._session is not None

    def get_aiohttp_session(self) -> aiohttp.ClientSession:
        if not self.initialized:
            self._session = aiohttp.ClientSession()
        return self._session

    async def api_call(self, method, token, data=None):
        """Slack API call."""
        session = self.get_aiohttp_session()
        form = aiohttp.FormData(data or {})
        form.add_field('token', token)
        async with session.post('https://slack.com/api/{0}'.format(method), data=form) as response:
            assert 200 == response.status, ('{0} with {1} failed.'
                                            .format(method, data))
            return await response.json()

    async def flush(self):
        pass

    async def emit(self, record: LogRecord):
        """
        Actually log the specified logging record to the slack.
        """
        try:
            channel = record.extra.get("channel", self.default_channel)
            msg = self.formatter.format(record)
            data = { "channel": channel, "text": msg, "as_user": True, "mrkdwn": True }
            method_name = "chat.postMessage"
            await run_coro(self.api_call(method_name, token=self.api_token, data=data))
        except Exception as exc:
            await self.handle_error(record, exc)

    async def close(self):
        """
        Tidy up any resources used by the handler.

        This version removes the handler from an internal map of handlers,
        should ensure that this gets called from overridden close()
        methods.
        """
        async def _close():
            await self.flush()
            await self._session.close()

        await run_coro(_close())
