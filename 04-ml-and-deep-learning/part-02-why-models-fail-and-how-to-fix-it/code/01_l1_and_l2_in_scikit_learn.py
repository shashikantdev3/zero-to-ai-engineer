"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 2 of 28
Slide: L1 and L2 in scikit-learn
Run: python 01_l1_and_l2_in_scikit_learn.py
"""
# Needs: pip install scikit-learn
from sklearn.linear_model import (
    LogisticRegression,
)
# L2 is the default
l2 = LogisticRegression(C=1.0)
# L1 gives sparse weights
l1 = LogisticRegression(
    penalty="l1", C=0.1, solver="liblinear"
)
