"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: Balanced Weights, Then Calibrate
Run: python 08_balanced_weights_then_calibrate.py
"""
# Needs: pip install scikit-learn
# --- repeated from 07_data_for_a_classifier.py so this file runs on its own ---
from sklearn.datasets import (
    make_classification)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import (
    StandardScaler)
from sklearn.linear_model import (
    LogisticRegression)
X, y = make_classification(n_samples=300,
    weights=[0.9], random_state=0)
X_train, X_val = X[:200], X[200:]
y_train = y[:200]

# --- this slide ---
lr = LogisticRegression(
    class_weight="balanced", max_iter=1000)
clf = make_pipeline(StandardScaler(), lr)
clf.fit(X_train, y_train)
proba = clf.predict_proba(X_val)[:, 1]
# balanced weights shift probabilities:
# calibrate before trusting them
print(proba[:5].round(2))
