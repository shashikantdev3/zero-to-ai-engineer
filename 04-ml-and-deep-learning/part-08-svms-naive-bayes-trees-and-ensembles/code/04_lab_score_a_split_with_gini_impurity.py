"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 8 of 28
Follow-along lab: Score a split with Gini impurity
Run: python 04_lab_score_a_split_with_gini_impurity.py
"""
def gini(ys):
    p = sum(ys) / len(ys)
    return round(1 - p**2 - (1 - p)**2, 3)

rows = [(10, 0), (20, 0), (30, 0),
        (60, 1), (70, 1), (80, 0)]
ys = [f for _, f in rows]
print("before split:", gini(ys))
for cut in (25, 50):
    lo = [f for a, f in rows if a <= cut]
    hi = [f for a, f in rows if a > cut]
    w = len(lo)*gini(lo) + len(hi)*gini(hi)
    print(f"cut {cut}:", round(w / len(ys), 3))
