"""Zero to AI Engineer · Evaluation · Part 2 of 11
Follow-along lab: See a leaky split
Run: python 03_lab_see_a_leaky_split.py
"""
cases = [(t, f"t{t}-v{v}") for t in range(6)
         for v in range(3)]
def leaks(dev, held):
    seen = {t for t, _ in dev}
    return sum(t in seen for t, _ in held)
# split by case: every third case held out
held = cases[::3]
dev = [c for c in cases if c not in held]
print("case split leaks:", leaks(dev, held))
# split by thread: threads 4 and 5 held out
gh = [c for c in cases if c[0] >= 4]
gd = [c for c in cases if c[0] < 4]
print("group split leaks:", leaks(gd, gh))
print("held-out sizes:", len(held), len(gh))
