"""Zero to AI Engineer · Security and Guardrails · Part 8 of 11
Follow-along lab: Choose a threshold by cost
Run: python 05_lab_choose_a_threshold_by_cost.py
"""
data = [(0, 0), (2, 0), (2, 1), (4, 0),
        (4, 1), (6, 1), (2, 0), (0, 0)]
FB_COST, MISS_COST = 1, 10
best = None
for t in (2, 4, 6):
    fb = sum(s >= t and not h
             for s, h in data)
    miss = sum(s < t and h for s, h in data)
    cost = fb * FB_COST + miss * MISS_COST
    print(f"block_at {t}: fb={fb} "
          f"miss={miss} cost={cost}")
    if best is None or cost < best[1]:
        best = (t, cost)
print(f"choose block_at {best[0]}")
