"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Calibrate, then check the curve
Run: python 06_calibrate_then_check_the_curve.py
"""
# Needs: pip install numpy scikit-learn
# --- repeated from 05_data_sorted_by_time.py so this file runs on its own ---
import numpy as np
from sklearn.calibration import (
    CalibratedClassifierCV, calibration_curve)
from sklearn.model_selection import (
    TimeSeriesSplit)
from sklearn.svm import LinearSVC
rng = np.random.default_rng(0)
X = rng.normal(size=(2000, 3))
noise = rng.normal(size=2000)
y = (X[:, 0] + noise > 1.5).astype(int)
X_tr, y_tr = X[:1500], y[:1500]
X_va, y_va = X[1500:], y[1500:]

# --- this slide ---
# rows are assumed sorted by time
base_model = LinearSVC()
cal = CalibratedClassifierCV(
    base_model, method="sigmoid",
    cv=TimeSeriesSplit(n_splits=5))
cal.fit(X_tr, y_tr)
p = cal.predict_proba(X_va)[:, 1]
frac_pos, mean_pred = calibration_curve(
    y_va, p, n_bins=10)
print(frac_pos.round(2))
print(mean_pred.round(2))
