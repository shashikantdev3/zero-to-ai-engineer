"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 25 of 28
Slide: Set up a suspect feature
Run: python 03_set_up_a_suspect_feature.py
"""
# Needs: pip install numpy scikit-learn
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
