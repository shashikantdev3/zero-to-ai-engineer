"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Follow-along lab: Watch PSI shrink with more rows
Run: python 03_lab_watch_psi_shrink_with_more_rows.py
"""
import math, random
random.seed(0)
def hist(xs, k=10):
    h = [1e-6] * k
    for x in xs: h[int(x * k)] += 1 / len(xs)
    return h
def psi(a, b):
    z = zip(hist(a), hist(b))
    return sum((p - q) * math.log(p / q)
               for p, q in z)
for n in (100, 1000, 10000):
    a = [random.random() for _ in range(n)]
    b = [random.random() for _ in range(n)]
    print(f"n={n}: PSI {psi(a, b):.3f}")
