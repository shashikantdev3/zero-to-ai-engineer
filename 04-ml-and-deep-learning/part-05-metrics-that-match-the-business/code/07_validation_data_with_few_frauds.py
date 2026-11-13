"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Validation data with few frauds
Run: python 07_validation_data_with_few_frauds.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import (
    average_precision_score as ap)
rng = np.random.default_rng(42)
y_val = (rng.random(300) < 0.1).astype(int)
s_old = y_val * 0.3 + rng.random(300)
s_new = y_val * 0.4 + rng.random(300)
n, diffs = len(y_val), []
print("positives:", y_val.sum())
