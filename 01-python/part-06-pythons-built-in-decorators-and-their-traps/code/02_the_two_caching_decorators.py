"""Zero to AI Engineer · Python · Part 6 of 25
Slide: The Two Caching Decorators
Run: python 02_the_two_caching_decorators.py
"""
from functools import cached_property
from functools import lru_cache
class Client:
    @cached_property
    def headers(self) -> dict:
        return {"User-Agent": "svc/1.0"}

@lru_cache(maxsize=1024)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
