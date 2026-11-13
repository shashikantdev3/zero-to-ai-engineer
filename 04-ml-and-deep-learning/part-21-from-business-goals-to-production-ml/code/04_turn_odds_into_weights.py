"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 21 of 28
Slide: Turn odds into weights
Run: python 04_turn_odds_into_weights.py
"""
# Needs: pip install numpy scikit-learn
# --- repeated from 03_train_a_domain_classifier.py so this file runs on its own ---
import numpy as np
from sklearn import linear_model as lm

rng = np.random.default_rng(0)
X_old = rng.normal(0.0, 1.0, (400, 2))
X_new = rng.normal(0.5, 1.0, (200, 2))
# Domain label: old rows 0, new rows 1
X = np.vstack([X_old, X_new])
y = np.r_[np.zeros(400), np.ones(200)]
dom = lm.LogisticRegression(max_iter=1000)
dom.fit(X, y)

# --- this slide ---
# Chance each old row looks "new"
p = dom.predict_proba(X_old)[:, 1]
# Odds, corrected for sample sizes
ratio = len(X_old) / len(X_new)
w = p / (1 - p) * ratio
print(round(w.mean(), 2))
