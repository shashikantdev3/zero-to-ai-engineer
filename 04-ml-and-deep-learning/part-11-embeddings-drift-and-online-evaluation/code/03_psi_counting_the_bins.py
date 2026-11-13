"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 11 of 28
Slide: PSI: counting the bins
Run: python 03_psi_counting_the_bins.py
"""
# Needs: pip install numpy
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
