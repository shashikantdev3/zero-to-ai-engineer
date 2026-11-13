"""Zero to AI Engineer · Python · Part 11 of 25
Follow-along lab: Safe Versus Leaky Cleanup
Run: python 03_lab_safe_versus_leaky_cleanup.py
"""
from contextlib import contextmanager
@contextmanager
def safe():
    try: yield
    finally: print("safe: cleanup ran")
@contextmanager
def leaky():
    yield
    print("leaky: cleanup ran")
for cm in (safe, leaky):
    try:
        with cm(): 1 / 0
    except ZeroDivisionError:
        print(cm.__name__ + ": error escaped")
