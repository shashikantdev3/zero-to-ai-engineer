"""Zero to AI Engineer · Python · Part 8 of 25
Follow-along lab: Watch the eager and lazy parts
Run: python 03_lab_watch_the_eager_and_lazy_parts.py
"""
data = [1, 2, 3]
g = (x for x in data)
data.append(4)
print("mutated:", list(g))
data = [1, 2, 3]
g = (x for x in data)
data = [9]
print("rebound:", list(g))
try:
    g = (x for x in None)
except TypeError:
    print("None fails at creation")
g = (x for x in [5, 0] if 10 // x)
print("filter runs lazily:", next(g))
