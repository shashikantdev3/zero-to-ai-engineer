"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 18 of 28
Slide: AUC from the Mann-Whitney U
Run: python 01_auc_from_the_mann_whitney_u.py
"""
# Needs: pip install numpy scipy scikit-learn
import numpy as np
from scipy.stats import mannwhitneyu
from sklearn.metrics import roc_auc_score
y = np.array([0, 0, 1, 1, 0, 1])
scores = np.array([.1, .4, .35, .8, .2, .9])
pos, neg = scores[y == 1], scores[y == 0]
u = mannwhitneyu(pos, neg).statistic
auc = u / (len(pos) * len(neg))
print(auc, roc_auc_score(y, scores))
