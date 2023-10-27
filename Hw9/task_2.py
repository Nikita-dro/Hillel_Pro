import requests
import functools
import tracemalloc


def memory_usage(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        memory = sum(stat.size for stat in snapshot.statistics('lineno')) / (1024*1024)
        print(f"Memory usage: {memory} MB")
        tracemalloc.stop()
        return result
    return deco


@memory_usage
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
