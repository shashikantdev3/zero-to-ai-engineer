"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: Plain Versus Ridge
Run: python 06_plain_versus_ridge.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.linear_model import (
    LinearRegression, Ridge)
X_train_s = np.array([[-1.0], [0.0], [1.0]])
y_train = np.array([1.0, 2.0, 3.1])
lin = LinearRegression()
lin.fit(X_train_s, y_train)
# alpha = L2 strength, larger = stronger
rid = Ridge(alpha=1.0)
rid.fit(X_train_s, y_train)
print(lin.coef_, rid.coef_)
