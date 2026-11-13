"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Slide: ROC-AUC Needs Scores
Run: python 04_roc_auc_needs_scores.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn.metrics import roc_auc_score

y_val = np.array([1, 0, 1, 1, 0, 0])
proba = np.array([.9, .8, .7, .3, .2, .6])
# proba = scores for the positive class
print(roc_auc_score(y_val, proba))
# hard 0/1 labels throw the ranking away
pred = (proba >= 0.5).astype(int)
print(roc_auc_score(y_val, pred))
