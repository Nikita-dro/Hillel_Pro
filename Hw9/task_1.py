import time
import functools
from collections import OrderedDict
import requests
import sys


def profile(msg='Elapsed time', file=sys.stdout):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            print(msg, f'({f.__name__}): {time.time() - start}s', file=file)
            return result
        return deco
    return internal


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._count[cache_key] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                min_value = min(deco._count.values())
                list_keys = [key for key, value in deco._count.items() if value == min_value]
                del deco._cache[list_keys[0]]
                del deco._count[list_keys[0]]
            deco._cache[cache_key] = result
            deco._count[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        deco._count = {}
        return deco

    return internal


@profile(msg='Elapsed time')
@cache(max_limit=3)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
fetch_url('https://ain.ua')
fetch_url('https://youtube.com')