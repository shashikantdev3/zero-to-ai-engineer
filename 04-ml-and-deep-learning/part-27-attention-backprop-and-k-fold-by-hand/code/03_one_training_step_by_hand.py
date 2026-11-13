"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: One training step by hand
Run: python 03_one_training_step_by_hand.py
"""
# Needs: pip install numpy
import numpy as np
def step(X, y, W1, b1, W2, b2, lr=0.01):
    n = len(X)
    z1 = X @ W1 + b1; a1 = np.maximum(0, z1)
    z2 = a1 @ W2 + b2
    dz2 = (z2 - y) / n
    dW2 = a1.T @ dz2; db2 = dz2.sum(0)
    # gate on z1, the pre-activation
    dz1 = (dz2 @ W2.T) * (z1 > 0)
    dW1 = X.T @ dz1; db1 = dz1.sum(0)
    return (W1 - lr * dW1, b1 - lr * db1,
            W2 - lr * dW2, b2 - lr * db2)
