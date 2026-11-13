"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Follow-along lab: Unscaled Neighbours Mislead
Run: python 10_lab_unscaled_neighbours_mislead.py
"""
pts = {"A": (52000, 61), "B": (50500, 24),
       "C": (90000, 60), "D": (49000, 26)}
q = (50000, 59)
print("query age", q[1])
def nearest(si, sa):
    def d(k):
        dx = (pts[k][0] - q[0]) / si
        dy = (pts[k][1] - q[1]) / sa
        return dx * dx + dy * dy
    return min(pts, key=d)
for name, si, sa in [("raw", 1, 1),
                     ("scaled", 20000, 20)]:
    k = nearest(si, sa)
    print(name, k, "age", pts[k][1])
