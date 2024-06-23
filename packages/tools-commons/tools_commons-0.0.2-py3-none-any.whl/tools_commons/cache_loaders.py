from tools_commons.registry import Registry


class CacheToolsRegistries(object):
    """Object holding `Registry` objects."""

    def __init__(self):
        raise RuntimeError("Registries is not intended to be instantiated")

    cache_loaders = Registry("cache_loaders")


list_cache_loaders = lambda: sorted(CacheToolsRegistries.cache_loaders)
register_cache_loader = CacheToolsRegistries.cache_loaders.register


@register_cache_loader("LRU")
def build_and_load_lru_cache(
        preloaded_dictionary=None, max_cache_size=1000, cache_buffer_multiplier=2, **kwargs
):
    if preloaded_dictionary is None:
        preloaded_dictionary = {}
    import cachetools

    cache = cachetools.LRUCache(
        maxsize=max_cache_size
        if len(preloaded_dictionary) == 0
        else min(len(preloaded_dictionary) * cache_buffer_multiplier, max_cache_size)
    )
    for key, val in preloaded_dictionary.items():
        cache[key] = val
    return cache


def cache_loader(cache_loader_name):
    return CacheToolsRegistries.cache_loaders[cache_loader_name]