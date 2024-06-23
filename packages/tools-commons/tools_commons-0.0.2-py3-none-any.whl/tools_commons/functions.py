import functools
from itertools import islice, chain


def compose(*functions):
    """Pipeline functions for sequential execution"""
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)


def batch(iterable, size):
    source_iter = iter(iterable)
    while True:
        batch_iter = islice(source_iter, size)
        try:
            yield chain([batch_iter.__next__()], batch_iter)
        except StopIteration:
            return
        # yield chain([batch_iter.__next__()], batch_iter)
