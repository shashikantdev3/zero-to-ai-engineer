"""Zero to AI Engineer · LLM Fundamentals · Part 18 of 18
Slide: Checking the Softmax Gradient
Run: python 01_checking_the_softmax_gradient.py
"""
# Needs: pip install numpy
import numpy as np
z = np.array([2.0, 1.0, 0.1])
y = np.array([1.0, 0.0, 0.0])
sm = lambda v: np.exp(v) / np.exp(v).sum()
p = sm(z)
J = np.diag(p) - np.outer(p, p)
L = lambda v: -np.log(sm(v) @ y)
h = 1e-6
num = np.array([(L(z + h*e) - L(z - h*e))
                / (2*h) for e in np.eye(3)])
print(np.allclose(num, p - y))
print(np.allclose(J @ (-y / p), p - y))
