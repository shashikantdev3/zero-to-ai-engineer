"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Follow-along lab: Break and fix a sigmoid
Run: python 04_lab_break_and_fix_a_sigmoid.py
"""
import math
def naive(z):
    return 1 / (1 + math.exp(-z))
def stable(z):
    e = math.exp(-abs(z))
    if z >= 0:
        return 1 / (1 + e)
    return e / (1 + e)
try:
    naive(-1000)
except OverflowError:
    print("naive: overflow at -1000")
for z in (-1000, 0, 1000):
    print(f"stable({z}) = {stable(z):.3f}")
