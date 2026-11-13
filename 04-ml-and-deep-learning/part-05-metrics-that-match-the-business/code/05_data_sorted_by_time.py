"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Data sorted by time
Run: python 05_data_sorted_by_time.py
"""
# Needs: pip install numpy scikit-learn
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
