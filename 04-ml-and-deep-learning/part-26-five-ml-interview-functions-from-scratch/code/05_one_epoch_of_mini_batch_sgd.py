"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: One epoch of mini-batch SGD
Run: python 05_one_epoch_of_mini_batch_sgd.py
"""
# Needs: pip install numpy
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
