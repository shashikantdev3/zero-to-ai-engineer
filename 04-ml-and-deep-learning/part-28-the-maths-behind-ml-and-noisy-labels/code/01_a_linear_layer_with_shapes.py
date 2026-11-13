"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Slide: A Linear Layer With Shapes
Run: python 01_a_linear_layer_with_shapes.py
"""
# Needs: pip install numpy
import numpy as np
X = np.random.randn(32, 10)  # (n=32, d=10)
W = np.random.randn(10, 4)  # (d=10, k=4)
b = np.zeros(4)  # (k,) broadcasts over rows
Z = X @ W + b  # (32, 4)
norms = np.linalg.norm(
    X, axis=1, keepdims=True)  # (32, 1)
Xn = X / norms  # unit rows
S = Xn @ Xn.T  # (32, 32) cosine sims
assert Z.shape == (32, 4)
assert S.shape == (32, 32)
