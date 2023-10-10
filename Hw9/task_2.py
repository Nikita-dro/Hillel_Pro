import requests
from memory_profiler import memory_usage


def memory_usage_decorator(f):
    def deco(*args, **kwargs):
        memory = memory_usage((f, args, kwargs))
        print(f"Memory usage: {memory[0]} MB")
        return f(*args, **kwargs)
    return deco


@memory_usage_decorator
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
