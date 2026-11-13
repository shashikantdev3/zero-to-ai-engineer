"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Slide: F1 and F-beta in Code
Run: python 02_f1_and_f_beta_in_code.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score
y_val = np.array([1, 0, 1, 1, 0, 0])
pred = np.array([1, 1, 1, 0, 0, 1])
print(f1_score(y_val, pred))
print(fbeta_score(y_val, pred, beta=2))
y_true_mc = ["cat", "dog", "cat", "bird"]
y_pred_mc = ["cat", "dog", "dog", "bird"]
print(f1_score(y_true_mc, y_pred_mc,
               average="macro"))
