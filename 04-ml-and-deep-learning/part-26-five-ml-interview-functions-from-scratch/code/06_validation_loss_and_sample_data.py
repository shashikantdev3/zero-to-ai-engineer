"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: Validation loss and sample data
Run: python 06_validation_loss_and_sample_data.py
"""
# Needs: pip install numpy
# --- repeated from 05_one_epoch_of_mini_batch_sgd.py so this file runs on its own ---
import numpy as np
def sigmoid(z):
    e = np.exp(-np.abs(z))
    return np.where(z >= 0, 1/(1+e), e/(1+e))
def epoch(X, y, w, b, idx, lr, lam, bs=32):
    for s in range(0, len(y), bs):
        j = idx[s:s + bs]
        p = sigmoid(X[j] @ w + b)
        g = X[j].T @ (p - y[j]) / len(j)
        w = w - lr * (g + lam * w)
        b = b - lr * (p - y[j]).mean()
    return w, b

# --- this slide ---
def logloss(X, y, w, b):
    p = np.clip(sigmoid(X @ w + b),
                1e-12, 1 - 1e-12)
    ll = y*np.log(p) + (1-y)*np.log(1-p)
    return -ll.mean()
rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)
Xv = rng.normal(size=(100, 2))
yv = (Xv[:, 0] + Xv[:, 1] > 0).astype(float)
EPOCHS, PATIENCE = 200, 10
