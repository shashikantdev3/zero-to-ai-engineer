"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: Computing the safe learning rate
Run: python 09_computing_the_safe_learning_rate.py
"""
# Needs: pip install numpy
# --- repeated from 08_linear_regression_by_gradient_descent.py so this file runs on its own ---
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

# --- this slide ---
def lr_max(X):
    # include the bias column
    Xa = np.c_[X, np.ones(len(X))]
    H = (2 / len(X)) * Xa.T @ Xa
    return 2 / np.linalg.eigvalsh(H).max()
rng = np.random.default_rng(0)
X = rng.normal(size=(100, 2)) * [1.0, 100.0]
Xs = (X - X.mean(0)) / X.std(0)
print(lr_max(X), lr_max(Xs))
