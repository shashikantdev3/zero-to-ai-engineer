"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Slide: Inflated Scores After Weighting
Run: python 06_inflated_scores_after_weighting.py
"""
# Needs: pip install numpy xgboost
# (not run while building this repo, because the package was not installed there)
# --- repeated from 05_scale_pos_weight_in_xgboost.py so this file runs on its own ---
import numpy as np
from xgboost import XGBClassifier
rng = np.random.default_rng(0)
X = rng.normal(size=(2000, 5))
y = (rng.random(2000) < 0.03).astype(int)
# rows are in time order: val is later
X_tr, y_tr = X[:1500], y[:1500]
X_val, y_val = X[1500:], y[1500:]
ratio = (y_tr == 0).sum() / (y_tr == 1).sum()
xgb = XGBClassifier(scale_pos_weight=ratio,
                    eval_metric="aucpr")
xgb.fit(X_tr, y_tr, eval_set=[(X_val, y_val)])

# --- this slide ---
# continues the code above
p = xgb.predict_proba(X_val)[:, 1]
print("mean score:", p.mean().round(3))
print("fraud rate:", y_val.mean().round(3))
# calibrate on time-ordered held-out data
