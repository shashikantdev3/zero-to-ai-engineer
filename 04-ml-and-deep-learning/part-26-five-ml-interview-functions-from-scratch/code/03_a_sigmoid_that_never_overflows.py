"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: A sigmoid that never overflows
Run: python 03_a_sigmoid_that_never_overflows.py
"""
# Needs: pip install numpy
import numpy as np

def sigmoid(z):
    e = np.exp(-np.abs(z))
    return np.where(z >= 0, 1 / (1 + e),
                    e / (1 + e))

z = np.array([-1000.0, 0.0, 1000.0])
with np.errstate(over="raise"):
    print(sigmoid(z))
