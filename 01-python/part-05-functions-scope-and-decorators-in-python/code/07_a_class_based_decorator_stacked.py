"""Zero to AI Engineer · Python · Part 5 of 25
Slide: A class-based decorator, stacked
Run: python 07_a_class_based_decorator_stacked.py
"""
# --- repeated from 06_a_retry_factory.py so this file runs on its own ---
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

# --- this slide ---
import functools
class CountCalls:
    def __init__(self, fn):
        functools.update_wrapper(self, fn)
        self.fn, self.calls = fn, 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.fn(*args, **kwargs)

@CountCalls
@retry(times=2)
def flaky(): return "ok"
