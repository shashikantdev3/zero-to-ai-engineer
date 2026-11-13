"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 2 of 28
Slide: Early stopping in LightGBM
Run: python 03_early_stopping_in_lightgbm.py
"""
# Needs: pip install lightgbm numpy
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
