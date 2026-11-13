"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 2 of 28
Slide: The scikit-learn version
Run: python 04_the_scikit_learn_version.py
"""
# Needs: pip install lightgbm numpy scikit-learn
# --- repeated from 03_early_stopping_in_lightgbm.py so this file runs on its own ---
import numpy as np
import lightgbm as lgb
rng = np.random.default_rng(0)
X = rng.normal(size=(400, 5))
y = (X[:, 0] > 0).astype(int)
# rows in time order: val comes later
X_tr, y_tr = X[:300], y[:300]
X_val, y_val = X[300:], y[300:]
clf = lgb.LGBMClassifier(
    n_estimators=1000, learning_rate=0.05)
clf.fit(X_tr, y_tr, eval_set=[(X_val, y_val)],
        callbacks=[lgb.early_stopping(20)])

# --- this slide ---
from sklearn.ensemble import (
    HistGradientBoostingClassifier,
)
# random split: use only on non-time data
clf2 = HistGradientBoostingClassifier(
    early_stopping=True,
    validation_fraction=0.1,
    n_iter_no_change=20,
    max_iter=1000,
)
clf2.fit(X, y)
