"""Zero to AI Engineer · Python · Part 11 of 25
Slide: A Timing Span With contextmanager
Run: python 01_a_timing_span_with_contextmanager.py
"""
import time
from contextlib import contextmanager
@contextmanager
def span(name: str):
    t = time.perf_counter()
    try:
        yield
    finally:
        took = time.perf_counter() - t
        print(f"{name}: {took:.3f}s")
with span("retrieve"):
    pass
