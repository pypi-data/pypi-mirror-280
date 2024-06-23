import asyncio
import threading

_started = False
_thread = None
_logging_event_loop = asyncio.new_event_loop()
_lock = threading.RLock()


async def get_logging_loop():
    global _logging_event_loop
    if not _started:
        start_thread()
    while not _logging_event_loop.is_running():
        await asyncio.sleep(0.1)
    return _logging_event_loop


def start_thread():
    global _thread
    global _started

    def _target():
        global _logging_event_loop
        asyncio.set_event_loop(_logging_event_loop)
        _logging_event_loop.run_forever()
        pending = asyncio.Task.all_tasks(loop=_logging_event_loop)
        _logging_event_loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
    with _lock:
        if not _started:
            _thread = threading.Thread(target=_target, daemon=True)
            _thread.start()
            _started = True


def stop_thread():
    global _logging_event_loop
    global _thread
    global _started
    if _started:
        with _lock:
            if _started:
                _started = False
                _logging_event_loop.call_soon_threadsafe(_logging_event_loop.stop)
                _thread.join()
                _thread = None


async def run_coro(coro) -> asyncio.Future:
    dst_fut = asyncio.get_event_loop().create_future()
    _log_loop = await get_logging_loop()
    src_fut = asyncio.ensure_future(coro, loop=_log_loop)
    asyncio.futures._chain_future(src_fut, dst_fut)
    _log_loop._write_to_self()
    return await dst_fut