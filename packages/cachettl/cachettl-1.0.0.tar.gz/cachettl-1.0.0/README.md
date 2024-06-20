# cachettl v1.0.0

An elegant LRU TTL Cache decorator with methods cache_info() and cache_clear()

More info about LRU (Last Recent Used) cache: https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)


```python
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

    """
``` 


## Installation
```bash
pip install cachettl
```

### Usage example:

```python
from cachettl import cachettl
import datetime as dt, time

@cachettl(ttl=4)
def print_datetime():
    return dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
if __name__ == '__main__':
    for I in range(15):
        print(f"{'%02d'%(I+1)}. {print_datetime()}")
        print(f"    CacheInfo: {print_datetime.cache_info()} - Only Remaining TTL: {print_datetime.cache_info().remainingttl}")
        time.sleep(0.5)
```

### Output:

```bash
01. 19/06/2024 20:54:34
    CacheInfo: CacheInfo(hits=0, misses=1, maxsize=128, currsize=1, remainingttl=3.999934673309326) - Only Remaining TTL: 3.999899387359619
02. 19/06/2024 20:54:34
    CacheInfo: CacheInfo(hits=1, misses=1, maxsize=128, currsize=1, remainingttl=3.4991674423217773) - Only Remaining TTL: 3.499129295349121
03. 19/06/2024 20:54:34
    CacheInfo: CacheInfo(hits=2, misses=1, maxsize=128, currsize=1, remainingttl=2.9986002445220947) - Only Remaining TTL: 2.998547315597534
04. 19/06/2024 20:54:34
    CacheInfo: CacheInfo(hits=3, misses=1, maxsize=128, currsize=1, remainingttl=2.4979164600372314) - Only Remaining TTL: 2.4978702068328857
05. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=3, misses=2, maxsize=128, currsize=2, remainingttl=3.9998769760131836) - Only Remaining TTL: 3.999843120574951
06. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=4, misses=2, maxsize=128, currsize=2, remainingttl=3.4992663860321045) - Only Remaining TTL: 3.499230146408081
07. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=5, misses=2, maxsize=128, currsize=2, remainingttl=2.9985880851745605) - Only Remaining TTL: 2.998532295227051
08. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=6, misses=2, maxsize=128, currsize=2, remainingttl=2.497987985610962) - Only Remaining TTL: 2.4979512691497803
09. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=7, misses=2, maxsize=128, currsize=2, remainingttl=1.9973821640014648) - Only Remaining TTL: 1.997338056564331
10. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=8, misses=2, maxsize=128, currsize=2, remainingttl=1.4968440532684326) - Only Remaining TTL: 1.4968063831329346
11. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=9, misses=2, maxsize=128, currsize=2, remainingttl=0.9962716102600098) - Only Remaining TTL: 0.9962363243103027
12. 19/06/2024 20:54:36
    CacheInfo: CacheInfo(hits=10, misses=2, maxsize=128, currsize=2, remainingttl=0.4957406520843506) - Only Remaining TTL: 0.49570631980895996
13. 19/06/2024 20:54:40
    CacheInfo: CacheInfo(hits=10, misses=3, maxsize=128, currsize=3, remainingttl=3.999873638153076) - Only Remaining TTL: 3.999840497970581
14. 19/06/2024 20:54:40
    CacheInfo: CacheInfo(hits=11, misses=3, maxsize=128, currsize=3, remainingttl=3.499295473098755) - Only Remaining TTL: 3.4992594718933105
15. 19/06/2024 20:54:40
    CacheInfo: CacheInfo(hits=12, misses=3, maxsize=128, currsize=3, remainingttl=2.9987926483154297) - Only Remaining TTL: 2.998769521713257

```

## Sugestions, feedbacks, bugs...
E-mail me: ricardoabuchaim at gmail.com
