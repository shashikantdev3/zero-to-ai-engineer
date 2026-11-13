"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Paired bootstrap of the difference
Run: python 08_paired_bootstrap_of_the_difference.py
"""
# Needs: pip install numpy scikit-learn
# --- repeated from 07_validation_data_with_few_frauds.py so this file runs on its own ---
import numpy as np
from sklearn.metrics import (
    average_precision_score as ap)
rng = np.random.default_rng(42)
y_val = (rng.random(300) < 0.1).astype(int)
s_old = y_val * 0.3 + rng.random(300)
s_new = y_val * 0.4 + rng.random(300)
n, diffs = len(y_val), []
print("positives:", y_val.sum())

# --- this slide ---
for _ in range(1000):
    # same resample for both models
    i = rng.integers(0, n, n)
    if y_val[i].sum() == 0:
        continue
    new = ap(y_val[i], s_new[i])
    old = ap(y_val[i], s_old[i])
    diffs.append(new - old)
# win only if lo > 0
lo, hi = np.percentile(diffs, [2.5, 97.5])
print(round(lo, 3), round(hi, 3))
