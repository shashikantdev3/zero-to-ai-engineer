"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: Linear regression by gradient descent
Run: python 08_linear_regression_by_gradient_descent.py
"""
# Needs: pip install numpy
import numpy as np
def fit_linear(X, y, lr=0.01, epochs=2000,
               lam=0.0):
    n, d = X.shape
    w, b = np.zeros(d), 0.0
    for _ in range(epochs):
        err = X @ w + b - y
        gw = 2 / n * (X.T @ err) + 2 * lam * w
        w = w - lr * gw
        b = b - lr * (2 / n) * err.sum()
    return w, b
