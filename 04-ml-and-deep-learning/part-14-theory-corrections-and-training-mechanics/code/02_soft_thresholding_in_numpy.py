"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 14 of 28
Slide: Soft-thresholding in NumPy
Run: python 02_soft_thresholding_in_numpy.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
# Lasso: coordinate descent, exact zeros
from sklearn.linear_model import Lasso
def soft_threshold(w, t):
    # proximal step for L1
    return np.sign(w) * np.maximum(
        np.abs(w) - t, 0.0)
w = np.array([0.8, 0.02, -0.01, -0.5])
lr, lam = 0.1, 0.5
# after each gradient step on the data loss
w = soft_threshold(w, lr * lam)
print(w)
