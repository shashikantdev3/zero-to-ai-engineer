"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: prf with zero-division guards
Run: python 02_prf_with_zero_division_guards.py
"""
# Needs: pip install numpy
import numpy as np
def prf(y, p):
    y, p = np.asarray(y), np.asarray(p)
    tp = int(((y == 1) & (p == 1)).sum())
    fp = int(((y == 0) & (p == 1)).sum())
    fn = int(((y == 1) & (p == 0)).sum())
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    s = prec + rec
    f1 = 2 * prec * rec / s if s else 0.0
    return prec, rec, f1
print(prf([1, 0, 1], [0, 0, 0]))
