import asyncio
import importlib
from importlib import util
from os.path import dirname, basename, isfile
from glob import glob
import threading
import time
import sys

import functools
from typing import List

IO_LOOP = None
thread = None


def start_new_loop():
    global IO_LOOP
    IO_LOOP = asyncio.new_event_loop()
    asyncio.set_event_loop(IO_LOOP)
    IO_LOOP.run_forever()
    if sys.version_info >= (3, 7):
        pending = asyncio.all_tasks(loop=IO_LOOP)
    else:
        pending = asyncio.Task.all_tasks(loop=IO_LOOP)
    coros = list()
    for _task in pending:
        _task.cancel()
        coros.append(_task)
    IO_LOOP.run_until_complete(asyncio.gather(*coros, return_exceptions=True))


def close_loop():
    global IO_LOOP
    global thread
    if IO_LOOP:
        IO_LOOP.call_soon_threadsafe(IO_LOOP.stop)
    if thread:
        thread.join()
    thread = None
    IO_LOOP = None


def load_module(_module):
    importlib.import_module(_module)
    loader = importlib.util.find_spec(_module).loader
    all_modules = [
        basename(f)[:-3]
        for f in glob(dirname(loader.get_filename()) + "/*.py")
        if isfile(f) and not f.endswith("__init__.py")
    ]
    for mod_ in all_modules:
        importlib.import_module("." + mod_, _module)


def load_single_module(_module):
    spec = util.spec_from_file_location(_module, _module)
    spec.loader.exec_module(util.module_from_spec(spec))


def run_co_routine(co_routine, create_event_loop=True):
    global thread
    global IO_LOOP

    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as ex:   # No event loop in thread.
        if create_event_loop:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        else:
            raise ex

    if loop.is_running():
        if not thread:
            thread = threading.Thread(target=start_new_loop, daemon=True)  # since even sys.exit will stop only the main thread.
            thread.start()
            while (not IO_LOOP) or (not IO_LOOP.is_running()):
                time.sleep(1)

        future = asyncio.run_coroutine_threadsafe(co_routine, IO_LOOP)
        return future.result()
    else:
        return loop.run_until_complete(co_routine)


# https://github.com/python/cpython/blob/master/Lib/asyncio/tasks.py
async def wait_for(fut, timeout):
    loop = asyncio.get_event_loop()

    if timeout is None:
        return await fut

    if timeout <= 0:
        fut = asyncio.ensure_future(fut, loop=loop)

        if fut.done():
            return fut.result()

        await _cancel_and_wait(fut, loop=loop)
        try:
            fut.result()
        except asyncio.CancelledError as exc:
            raise asyncio.TimeoutError() from exc
        else:
            raise asyncio.TimeoutError()

    waiter = loop.create_future()
    timeout_handle = loop.call_later(timeout, _release_waiter, waiter)
    cb = functools.partial(_release_waiter, waiter)

    fut = asyncio.ensure_future(fut, loop=loop)
    fut.add_done_callback(cb)

    try:
        # wait until the future completes or the timeout
        try:
            await waiter
        except asyncio.CancelledError:
            if fut.done():
                return fut.result()
            else:
                fut.remove_done_callback(cb)
                # We must ensure that the task is not running
                # after wait_for() returns.
                # See https://bugs.python.org/issue32751
                await _cancel_and_wait(fut, loop=loop)
                raise

        if fut.done():
            return fut.result()
        else:
            fut.remove_done_callback(cb)
            # We must ensure that the task is not running
            # after wait_for() returns.
            # See https://bugs.python.org/issue32751
            await _cancel_and_wait(fut, loop=loop)
            # In case task cancellation failed with some
            # exception, we should re-raise it
            # See https://bugs.python.org/issue40607
            try:
                fut.result()
            except asyncio.CancelledError as exc:
                raise asyncio.TimeoutError() from exc
            else:
                raise asyncio.TimeoutError()
    finally:
        timeout_handle.cancel()


async def _cancel_and_wait(fut, loop):
    waiter = loop.create_future()
    cb = functools.partial(_release_waiter, waiter)
    fut.add_done_callback(cb)

    try:
        fut.cancel()
        await waiter
    finally:
        fut.remove_done_callback(cb)


def _release_waiter(waiter, *args):
    if not waiter.done():
        waiter.set_result(None)


async def semaphore_gather(
    coroutines: List, semaphore: asyncio.Semaphore, return_exceptions=False
):
    async def _wrap_coro(coroutine):
        async with semaphore:
            return await coroutine

    return await asyncio.gather(
        *(_wrap_coro(coroutine) for coroutine in coroutines),
        return_exceptions=return_exceptions
    )



