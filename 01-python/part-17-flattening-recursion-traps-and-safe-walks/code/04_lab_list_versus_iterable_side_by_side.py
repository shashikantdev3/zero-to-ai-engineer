"""Zero to AI Engineer · Python · Part 17 of 25
Follow-along lab: List versus Iterable, side by side
Run: python 04_lab_list_versus_iterable_side_by_side.py
"""
from collections.abc import Iterable
def flat(lst, test):
    for item in lst:
        if isinstance(item, test):
            yield from flat(item, test)
        else:
            yield item
data = [1, [2, [3, "ab"]], []]
print(list(flat(data, list)))
print("first:", next(flat(data, list)))
try:
    list(flat(data, Iterable))
except RecursionError:
    print("Iterable: RecursionError")
