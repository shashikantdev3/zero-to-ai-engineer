"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 25 of 28
Slide: Shapes stated before the maths
Run: python 05_shapes_stated_before_the_maths.py
"""
# Needs: pip install numpy
import numpy as np
n, d = 4, 3
# X is n by d
X = np.ones((n, d))
# w is d
w = np.zeros(d)
# so X @ w is n
print((X @ w).shape)
