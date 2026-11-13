"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 11 of 28
Slide: PSI: the score itself
Run: python 04_psi_the_score_itself.py
"""
# Needs: pip install numpy
# --- repeated from 03_psi_counting_the_bins.py so this file runs on its own ---
import numpy as np

def counts(expected, actual, bins=10):
    qs = np.linspace(0, 1, bins + 1)
    cuts = np.quantile(expected, qs)
    # drop repeated edges
    edges = np.unique(cuts)
    e = np.histogram(expected, edges)[0]
    lo, hi = edges[0], edges[-1]
    clipped = np.clip(actual, lo, hi)
    a = np.histogram(clipped, edges)[0]
    return e.astype(float), a.astype(float)

# --- this slide ---
def psi(expected, actual, bins=10, eps=1e-6):
    e, a = counts(expected, actual, bins)
    # epsilon first, so each sums to 1
    e = (e + eps) / (e + eps).sum()
    a = (a + eps) / (a + eps).sum()
    return np.sum((a - e) * np.log(a / e))

rng = np.random.default_rng(0)
old = rng.normal(0, 1, 5000)
new = rng.normal(0.5, 1, 5000)
print(round(psi(old, new), 3))
