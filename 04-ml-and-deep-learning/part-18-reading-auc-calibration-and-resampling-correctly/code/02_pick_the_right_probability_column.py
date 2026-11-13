"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 18 of 28
Slide: Pick the right probability column
Run: python 02_pick_the_right_probability_column.py
"""
# Needs: pip install numpy scipy scikit-learn
# --- repeated from 01_auc_from_the_mann_whitney_u.py so this file runs on its own ---
import numpy as np
from scipy.stats import mannwhitneyu
from sklearn.metrics import roc_auc_score
y = np.array([0, 0, 1, 1, 0, 1])
scores = np.array([.1, .4, .35, .8, .2, .9])
pos, neg = scores[y == 1], scores[y == 0]
u = mannwhitneyu(pos, neg).statistic
auc = u / (len(pos) * len(neg))
print(auc, roc_auc_score(y, scores))

# --- this slide ---
from sklearn.linear_model import (
    LogisticRegression,
)
from sklearn.metrics import (
    average_precision_score,
)
X = scores.reshape(-1, 1)
clf = LogisticRegression().fit(X, y)
assert set(clf.classes_) == {0, 1}
col = list(clf.classes_).index(1)
proba = clf.predict_proba(X)[:, col]
print(average_precision_score(y, proba))
