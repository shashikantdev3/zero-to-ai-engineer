"""Zero to AI Engineer · Python · Part 5 of 25
Slide: A timing decorator
Run: python 04_a_timing_decorator.py
"""
import functools, time

def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            dt = time.perf_counter() - t
            print(f"{fn.__name__}: {dt:.3f}s")
    return wrapper
