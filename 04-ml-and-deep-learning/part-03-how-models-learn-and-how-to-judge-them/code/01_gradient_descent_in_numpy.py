"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 3 of 28
Slide: Gradient Descent in NumPy
Run: python 01_gradient_descent_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([3.0, 5.0, 7.0, 9.0])
w, b, lr = 0.0, 0.0, 0.01
for _ in range(1000):
    pred = w * x + b
    # gradient of mean squared error
    dw = 2 * np.mean((pred - y) * x)
    db = 2 * np.mean(pred - y)
    w, b = w - lr * dw, b - lr * db
print(round(w, 2), round(b, 2))
