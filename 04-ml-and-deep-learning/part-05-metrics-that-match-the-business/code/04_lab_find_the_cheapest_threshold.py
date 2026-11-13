"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Follow-along lab: Find the cheapest threshold
Run: python 04_lab_find_the_cheapest_threshold.py
"""
ys = [1, 0, 1, 0, 0, 1, 0, 0]
sc = [.9, .8, .7, .6, .4, .3, .2, .1]
amt = [500, 0, 80, 0, 0, 900, 0, 0]
FP_COST = 50
costs = {}
for t in (0.75, 0.5, 0.25):
    fn = sum(a for y, s, a in zip(ys, sc, amt)
             if y == 1 and s < t)
    fp = sum(1 for y, s in zip(ys, sc)
             if y == 0 and s >= t)
    costs[t] = fn + FP_COST * fp
    print(f"t={t} fp={fp} cost={costs[t]}")
best = min(costs, key=costs.get)
print("best:", best, "cost:", costs[best])
