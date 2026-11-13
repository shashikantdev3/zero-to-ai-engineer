"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Slide: A PSI function
Run: python 01_a_psi_function.py
"""
# Needs: pip install numpy
import numpy as np

def psi(ref, cur, bins=10):
    edges = np.histogram_bin_edges(ref, bins)
    cur = np.clip(cur, edges[0], edges[-1])
    p = np.histogram(ref, edges)[0] / len(ref)
    q = np.histogram(cur, edges)[0] / len(cur)
    p, q = p + 1e-6, q + 1e-6
    return np.sum((p - q) * np.log(p / q))
