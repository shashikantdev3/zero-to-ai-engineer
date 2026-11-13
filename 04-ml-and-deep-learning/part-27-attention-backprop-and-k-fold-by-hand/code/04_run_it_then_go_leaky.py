"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: Run it, then go leaky
Run: python 04_run_it_then_go_leaky.py
"""
# Needs: pip install numpy
# --- repeated from 03_one_training_step_by_hand.py so this file runs on its own ---
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

# --- this slide ---
rng = np.random.default_rng(0)
X = rng.normal(size=(8, 3))
y = rng.normal(size=(8, 1))
p = (rng.normal(size=(3, 4)), np.zeros(4),
     rng.normal(size=(4, 1)), np.zeros(1))
for _ in range(200):
    p = step(X, y, *p)
z1 = X @ p[0] + p[1]
z2 = np.maximum(0, z1) @ p[2] + p[3]
print(0.5 * ((z2 - y) ** 2).mean())
# leaky ReLU: the mask depends on z1
leaky = np.where(z1 > 0, 1.0, 0.01)
