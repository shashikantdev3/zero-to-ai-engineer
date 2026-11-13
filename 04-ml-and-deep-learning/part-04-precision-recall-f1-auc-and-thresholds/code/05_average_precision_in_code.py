"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Slide: Average Precision in Code
Run: python 05_average_precision_in_code.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn import metrics

y_val = np.array([1, 0, 0, 1, 0, 0])
proba = np.array([.9, .8, .7, .6, .2, .1])
ap = metrics.average_precision_score(
    y_val, proba)
curve = metrics.precision_recall_curve
prec, rec, thr = curve(y_val, proba)
print(round(ap, 3))
print("base rate:", round(y_val.mean(), 3))
