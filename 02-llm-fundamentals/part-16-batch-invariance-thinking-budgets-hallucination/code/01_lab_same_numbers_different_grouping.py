"""Zero to AI Engineer · LLM Fundamentals · Part 16 of 18
Follow-along lab: Same numbers, different grouping
Run: python 01_lab_same_numbers_different_grouping.py
"""
from functools import reduce
def add(xs):
    return reduce(lambda a, b: a + b, xs, 0.0)
def grouped(xs, n):
    parts = [add(xs[i:i + n])
             for i in range(0, len(xs), n)]
    return add(parts)
vals = [0.1] * 10
g1, g5 = grouped(vals, 1), grouped(vals, 5)
print("groups of 1:", g1)
print("groups of 5:", g5)
print("rerun same:", g1 == grouped(vals, 1))
print("1 vs 5 equal:", g1 == g5)
