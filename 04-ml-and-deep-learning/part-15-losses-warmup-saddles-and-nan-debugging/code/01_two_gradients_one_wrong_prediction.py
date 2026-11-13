"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 15 of 28
Slide: Two gradients, one wrong prediction
Run: python 01_two_gradients_one_wrong_prediction.py
"""
# Needs: pip install numpy
import numpy as np

z = np.array([-6.0])
y = 1.0
p = 1 / (1 + np.exp(-z))
# cross-entropy gradient on the logit
grad_ce = p - y
# squared error gradient via sigmoid
grad_mse = 2 * (p - y) * p * (1 - p)
print(grad_ce, grad_mse)
