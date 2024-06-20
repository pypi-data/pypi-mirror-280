#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
"""CacheTTL - An elegant TTL Cache decorator with methods cache_info() and cache_clear()"""
"""
                _         _____ _____ _
  ___ __ _  ___| |__   __|_   _|_   _| |
 / __/ _` |/ __| '_ \ / _ \| |   | | | |
| (_| (_| | (__| | | |  __/| |   | | | |___
 \___\__,_|\___|_| |_|\___||_|   |_| |_____|

  Author.: Ricardo Abuchaim - ricardoabuchaim@gmail.com
  License: MIT
  Github.: https://github.com/rabuchaim/cachettl
  PyPI...: https://pypi.org/project/cachettl/  ( pip install cachettl )

"""
import functools, time
from collections import namedtuple

__all__ = ["cachettl","cachettl_min"]

##──── A cache decorator that uses time to live with methods cache_info() and cache_clear() ─────────────────────────────────────────────────────────────────────────────────────────────
def cachettl(ttl=60, maxsize=128, typed=False):
    """An elegant TTL Cache decorator with methods cache_info() and cache_clear()
        
    If *maxsize* is set to None, the LRU features are disabled and the cache
    can grow without bound.

    If *typed* is True, arguments of different types will be cached separately.
    For example, f(3.0) and f(3) will be treated as distinct calls with
    distinct results.

    Arguments to the cached function must be hashable.

    View the cache statistics named tuple (hits, misses, maxsize, currsize and remainingttl)
    with f.cache_info().  Clear the cache and statistics with f.cache_clear().
    
    Access the underlying function with f._wrapped.

    See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
    
    """
    def _decorator(func):
        CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize", "remainingttl"])
        insertion_times = {}

        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def _new_lrucache(*args, __time_modificator, **kwargs):
            result = func(*args, **kwargs)
            insertion_times[args] = time.time()
            return result

        @functools.wraps(func)
        def _wrapped(*args, **kwargs):
            return _new_lrucache(*args, **kwargs, __time_modificator=int(int(time.time()) / ttl))

        def cache_info():
            info = _new_lrucache.cache_info()
            if insertion_times:
                first_key = next(iter(insertion_times))
                remaining_ttl = ttl - (time.time() - insertion_times[first_key])
            else:
                remaining_ttl = 0
            return CacheInfo(info.hits,info.misses,info.maxsize,info.currsize,remaining_ttl)

        def cache_clear():
            insertion_times.clear()
            return _new_lrucache.cache_clear()

        _wrapped.cache_info = cache_info
        _wrapped.cache_clear = cache_clear
        return _wrapped

    return _decorator

##──── A minimal version of cachettl without methods cache_info() and cache_clear() ────────────────────────────────────────────────────────────────────
def cachettl_min(ttl=60, maxsize=128, typed=False):
    """A minimal version of cachettl decorator without methods cache_info() and cache_clear()"""
    
    def _decorator(func):
        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def _new_lrucache(*args, __time_modificator, **kwargs):
            return func(*args, **kwargs)

        @functools.wraps(func)
        def _wrapped(*args, **kwargs):
            return _new_lrucache(*args, **kwargs, __time_modificator=int(int(time.time()) / ttl))

        return _wrapped

    return _decorator
