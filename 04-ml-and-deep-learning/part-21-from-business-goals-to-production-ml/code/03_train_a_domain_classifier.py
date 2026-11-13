"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 21 of 28
Slide: Train a domain classifier
Run: python 03_train_a_domain_classifier.py
"""
# Needs: pip install numpy scikit-learn
import numpy as np
from sklearn import linear_model as lm

rng = np.random.default_rng(0)
X_old = rng.normal(0.0, 1.0, (400, 2))
X_new = rng.normal(0.5, 1.0, (200, 2))
# Domain label: old rows 0, new rows 1
X = np.vstack([X_old, X_new])
y = np.r_[np.zeros(400), np.ones(200)]
dom = lm.LogisticRegression(max_iter=1000)
dom.fit(X, y)
