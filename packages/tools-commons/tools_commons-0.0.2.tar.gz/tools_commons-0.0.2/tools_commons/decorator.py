import asyncio
import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)


def retry(exception_to_check, tries=4, delay=3, back_off=2, logger=None):
    """Retry calling the decorated function using an exponential back_off.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param exception_to_check: the exception to check. may be a tuple of
        exceptions to check
    :type exception_to_check: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param back_off: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type back_off: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """

    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exception_to_check as e:
                    msg = "%s, Retrying in %.1f seconds..." % (str(e), mdelay)
                    if logger:
                        logger.error(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= back_off
            return f(*args, **kwargs)

        async def async_f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return await f(*args, **kwargs)
                except exception_to_check as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    await asyncio.sleep(mdelay)
                    mtries -= 1
                    mdelay *= back_off
            return await f(*args, **kwargs)

        if asyncio.iscoroutinefunction(f):
            return async_f_retry
        return f_retry  # true decorator
    return deco_retry


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            msg = "%r  %2.2f ms" % (method.__name__, (te - ts) * 1000)
            logger.warning(msg)
        return result

    async def async_timed(*args, **kw):
        ts = time.time()
        result = await method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            msg = "%r  %2.2f ms" % (method.__name__, (te - ts) * 1000)
            logger.warning(msg)
        return result

    if asyncio.iscoroutinefunction(method):
        return async_timed
    return timed
