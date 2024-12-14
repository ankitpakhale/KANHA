from typing import Any, Callable
import diskcache as dc
from functools import wraps
from utils import logger
import hashlib


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

    @staticmethod
    def generate_cache_key(func: Callable, args: tuple, kwargs: dict) -> str:
        """
        Generates a unique cache key based on function name, args, and kwargs.
        """
        # convert arguments to their string representation, avoiding memory addresses
        func_name = func.__name__
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in sorted(kwargs.items())]

        # combine everything into a single string
        key_data = f"{func_name}-{'-'.join(args_repr)}-{'-'.join(kwargs_repr)}"

        # generate a hash for consistent and unique key
        cache_key = hashlib.sha256(key_data.encode("utf-8")).hexdigest()
        return cache_key


# object of cache_manager
cache_manager = CacheManager()


def cache(func):
    """
    Custom decorator to cache the result using CacheManager.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = cache_manager.generate_cache_key(func, args, kwargs)
        logger.info(f"Cache_key: {cache_key}")

        # check if the result is cached
        cached_result = cache_manager.get(cache_key)
        if cached_result:
            logger.info(f"Cache hit for key: {cache_key}")
            return cached_result

        # call the original function to generate the result
        result = func(*args, **kwargs)

        # cache the result
        cache_manager.set(cache_key, result)
        logger.warning(f"Cache miss for key: {cache_key}. Caching the result.")
        return result

    return wrapper


def delete_cache(_key):
    cache_manager.delete(_key)


def clear_cache():
    cache_manager.clear()
