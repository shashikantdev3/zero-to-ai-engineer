"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: Fit on Train, Apply Everywhere
Run: python 03_fit_on_train_apply_everywhere.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.preprocessing import (
    StandardScaler)
X_train = np.array([[50.0, 25], [90.0, 40],
                    [30.0, 60]])
X_val = np.array([[70.0, 35]])
# fit on training data only
sc = StandardScaler().fit(X_train)
X_train_s = sc.transform(X_train)
X_val_s = sc.transform(X_val)
print(X_train_s.round(2))
print(X_val_s.round(2))
