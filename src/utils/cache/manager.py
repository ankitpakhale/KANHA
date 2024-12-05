from typing import Any
import diskcache as dc
from functools import wraps
from utils import __logger


class CacheManager:
    """
    CacheManager handles caching operations using a dictionary for now.
    """

    # diskcache configurations
    cache_store = dc.Cache(".kanha_cache")

    @staticmethod
    def get(key: str) -> Any:
        """
        get value from cache by key
        """
        return CacheManager.cache_store.get(key)

    @staticmethod
    def set(key: str, value: Any) -> None:
        """
        set value in cache by key
        """
        CacheManager.cache_store[key] = value

    @staticmethod
    def has(key: str) -> bool:
        """
        check if key exists in cache
        """
        return key in CacheManager.cache_store

    @staticmethod
    def delete(key: str) -> None:
        """
        Delete a specific cache entry by key.
        """
        if CacheManager.has(key):
            del CacheManager.cache_store[key]

    @staticmethod
    def clear() -> None:
        """
        Clear all cache entries.
        """
        CacheManager.cache_store.clear()


# object of cache_manager
cache_manager = CacheManager()


def __cache(func):
    """
    Custom decorator to cache the result using CacheManager.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # generate a cache key based on function arguments
        # FIXME: fix the generation of cache key
        cache_key = (
            f"{func.__name__}-"
            + "-".join(str(arg) for arg in args)
            + "-"
            + "-".join(f"{k}={v}" for k, v in kwargs.items())
        )
        print("➡ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> cache_key:", cache_key)

        # check if the result is cached
        cached_result = cache_manager.get(cache_key)
        if cached_result:
            __logger.debug(f"Cache hit for key: {cache_key}")
            return cached_result

        # call the original function to generate the result
        result = func(*args, **kwargs)

        # cache the result
        cache_manager.set(cache_key, result)
        __logger.debug(f"Cache miss for key: {cache_key}. Caching the result.")
        return result

    return wrapper


def __delete_cache(_key):
    cache_manager.delete(_key)
    __logger.debug(f"Cache deleted for key '{_key}'!!!")


def __clear_cache():
    cache_manager.clear()
    __logger.debug("Deleted all caches!!!")
