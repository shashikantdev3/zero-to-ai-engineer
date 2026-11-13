"""Zero to AI Engineer · Python · Part 5 of 25
Slide: A retry factory
Run: python 06_a_retry_factory.py
"""
import functools
def retry(times=3, on=(TimeoutError,)):
    if times < 1: raise ValueError(times)
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return fn(*args, **kwargs)
                except on:
                    if i == times - 1: raise
        return functools.wraps(fn)(wrapper)
    return decorator
