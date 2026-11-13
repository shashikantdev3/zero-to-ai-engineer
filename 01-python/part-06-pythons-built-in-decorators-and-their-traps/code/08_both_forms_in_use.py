"""Zero to AI Engineer · Python · Part 6 of 25
Slide: Both Forms in Use
Run: python 08_both_forms_in_use.py
"""
# --- repeated from 07_the_retry_decorator.py so this file runs on its own ---
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

# --- this slide ---
# bare: the function arrives directly
@retry
def a(): return "a"

# with options: partial, then the function
@retry(times=5)
def b(): return "b"
