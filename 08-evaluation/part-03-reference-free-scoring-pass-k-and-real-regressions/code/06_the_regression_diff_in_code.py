"""Zero to AI Engineer · Evaluation · Part 3 of 11
Slide: The regression diff in code
Run: python 06_the_regression_diff_in_code.py
"""
def regressions(old, new, critical):
    broke = [c for c in old
        if old[c] and not new.get(c, False)]
    fixed = [c for c in old
        if not old[c] and new.get(c, False)]
    blocking = [c for c in broke
                if c in critical]
    return broke, fixed, blocking

old = {"q1": True, "q2": False, "q3": True}
new = {"q1": False, "q2": True, "q3": True}
print(regressions(old, new, critical={"q1"}))
