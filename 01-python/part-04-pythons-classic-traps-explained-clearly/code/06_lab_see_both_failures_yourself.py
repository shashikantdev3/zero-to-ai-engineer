"""Zero to AI Engineer · Python · Part 4 of 25
Follow-along lab: See Both Failures Yourself
Run: python 06_lab_see_both_failures_yourself.py
"""
d = {"a": 1, "b": 2, "c": 1}
try:
    for k in d:
        if d[k] == 1:
            del d[k]
except RuntimeError as e:
    print("dict raised", type(e).__name__)
xs = [1, 1, 2, 3]
for x in xs:
    if x == 1:
        xs.remove(x)
print("list result:", xs)
ys = [x for x in [1, 1, 2, 3] if x != 1]
print("comprehension:", ys)
