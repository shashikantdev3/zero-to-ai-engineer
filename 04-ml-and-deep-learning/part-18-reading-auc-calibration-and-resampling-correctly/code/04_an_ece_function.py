"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 18 of 28
Slide: An ECE function
Run: python 04_an_ece_function.py
"""
# Needs: pip install numpy
import numpy as np
def ece(y, p, bins=10):
    edges = np.linspace(0, 1, bins + 1)
    idx = np.digitize(p, edges[1:-1])
    idx = np.clip(idx, 0, bins - 1)
    total = 0.0
    for b in range(bins):
        m = idx == b
        if m.any():
            gap = y[m].mean() - p[m].mean()
            total += m.mean() * abs(gap)
    return total
