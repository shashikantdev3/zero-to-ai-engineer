"""Zero to AI Engineer · Evaluation · Part 9 of 11
Follow-along lab: Pick the Cheapest Passing Judge
Run: python 03_lab_pick_the_cheapest_passing_judge.py
"""
judges = [("big", 0.82, 0.91, 9.0),
          ("mid", 0.79, 0.88, 2.0),
          ("small", 0.64, 0.71, 0.4)]
def clears(j):
    return j[1] >= 0.75 and j[2] >= 0.85
for j in judges:
    tag = "clears" if clears(j) else "below"
    print(f"{j[0]}: kappa {j[1]} {tag}")
ok = [j for j in judges if clears(j)]
best = min(ok, key=lambda j: j[3])
print(f"pick {best[0]} at ${best[3]}/1k")
