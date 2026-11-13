"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 18 of 28
Slide: Same data, different bins
Run: python 05_same_data_different_bins.py
"""
# Needs: pip install numpy scikit-learn
# --- repeated from 04_an_ece_function.py so this file runs on its own ---
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

# --- this slide ---
from sklearn.metrics import brier_score_loss
y = np.array([0, 1, 0, 0, 1, 1])
p = np.array([.2, .7, .9, .4, .6, .8])
print(ece(y, p, bins=10))
print(ece(y, p, bins=2))
print(brier_score_loss(y, p))
