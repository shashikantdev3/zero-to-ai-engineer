"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 25 of 28
Slide: Ablate and re-evaluate
Run: python 04_ablate_and_re_evaluate.py
"""
# Needs: pip install numpy scikit-learn
# --- repeated from 03_set_up_a_suspect_feature.py so this file runs on its own ---
import numpy as np
from sklearn.linear_model import (
    LogisticRegression)
from sklearn.metrics import (
    average_precision_score as ap)
rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
# column 1 is the suspect feature
y = (X[:, 1] + 0.3 * rng.normal(size=400)
     > 0).astype(int)
X_tr, X_val = X[:300], X[300:]
y_tr, y_val = y[:300], y[300:]

# --- this slide ---
model = LogisticRegression().fit(X_tr, y_tr)
X_abl = X_val.copy()
# replace it with its training median
X_abl[:, 1] = np.median(X_tr[:, 1])
p_val = model.predict_proba(X_val)[:, 1]
p_abl = model.predict_proba(X_abl)[:, 1]
# direct evaluation, before and after
print(ap(y_val, p_val))
print(ap(y_val, p_abl))
