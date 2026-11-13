"""Zero to AI Engineer · Python · Interview Quiz
Slide: Flatten a nested list
Run: python 01_flatten_a_nested_list.py
"""
from collections.abc import Iterable
def flat(xs):
    for x in xs:
        if isinstance(x, Iterable):
            yield from flat(x)
        else:
            yield x
try:
    print(list(flat([1, [2, [3, "ab"]]])))
except RecursionError as e:
    print(type(e).__name__)
