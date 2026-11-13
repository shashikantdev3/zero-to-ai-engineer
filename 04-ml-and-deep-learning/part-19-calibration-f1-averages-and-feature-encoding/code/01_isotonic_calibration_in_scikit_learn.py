"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 19 of 28
Slide: Isotonic calibration in scikit-learn
Run: python 01_isotonic_calibration_in_scikit_learn.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn import linear_model, calibration
from sklearn import model_selection as ms
rng = np.random.default_rng(0)
X_train = rng.normal(size=(300, 3))
y_train = (X_train[:, 0] > 0).astype(int)
base = linear_model.LogisticRegression()
# "sigmoid" = Platt; cv=5 if not temporal
cal = calibration.CalibratedClassifierCV(
    base, method="isotonic",
    cv=ms.TimeSeriesSplit(n_splits=5))
cal.fit(X_train, y_train)
