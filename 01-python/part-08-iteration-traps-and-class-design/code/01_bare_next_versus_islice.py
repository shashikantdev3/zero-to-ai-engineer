"""Zero to AI Engineer · Python · Part 8 of 25
Slide: Bare next versus islice
Run: python 01_bare_next_versus_islice.py
"""
from itertools import islice

def first_n_bad(it, n):
    it = iter(it)
    for _ in range(n):
        # 3.7+: RuntimeError if it runs out
        yield next(it)

def first_n(it, n):
    yield from islice(it, n)
print(list(first_n([1, 2], 5)))
# list(first_n_bad([1, 2], 5))
