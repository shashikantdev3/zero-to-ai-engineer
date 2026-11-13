"""Zero to AI Engineer · Python · Part 6 of 25
Slide: The Retry Decorator
Run: python 07_the_retry_decorator.py
"""
from functools import partial, wraps
def retry(fn=None, *, times=3):
    if fn is None:
        return partial(retry, times=times)
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for attempt in range(times):
            try:
                return fn(*args, **kwargs)
            except TimeoutError:
                if attempt == times - 1: raise
    return wrapper
