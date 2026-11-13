"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Slide: Precision and Recall in Code
Run: python 01_precision_and_recall_in_code.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

y_val = np.array([1, 0, 1, 1, 0, 0])
proba = np.array([.9, .8, .7, .3, .2, .6])
thr = 0.5
pred = (proba >= thr).astype(int)
print(precision_score(y_val, pred))
print(recall_score(y_val, pred))
