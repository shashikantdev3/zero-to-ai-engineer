"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Slide: An alert level from resampling
Run: python 02_an_alert_level_from_resampling.py
"""
# Needs: pip install numpy
# --- repeated from 01_a_psi_function.py so this file runs on its own ---
import numpy as np

def psi(ref, cur, bins=10):
    edges = np.histogram_bin_edges(ref, bins)
    cur = np.clip(cur, edges[0], edges[-1])
    p = np.histogram(ref, edges)[0] / len(ref)
    q = np.histogram(cur, edges)[0] / len(cur)
    p, q = p + 1e-6, q + 1e-6
    return np.sum((p - q) * np.log(p / q))

# --- this slide ---
def psi_null(ref, n, trials=500, seed=0):
    rng = np.random.default_rng(seed)
    ds = [rng.choice(ref, n)
          for _ in range(trials)]
    return np.array([psi(ref, d) for d in ds])

rng = np.random.default_rng(1)
x_ref = rng.normal(0, 1, 5000)
x_live = rng.normal(0, 1, 100)
null = psi_null(x_ref, len(x_live))
alert_level = np.percentile(null, 99)
print(round(alert_level, 3))
