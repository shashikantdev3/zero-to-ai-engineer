"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 8 of 28
Slide: Boosting with early stopping
Run: python 06_boosting_with_early_stopping.py
"""
# Needs: pip install scikit-learn
from sklearn import datasets
from sklearn.ensemble import (
    HistGradientBoostingClassifier)
d = datasets.load_breast_cancer()
X_train, y_train = d.data, d.target
gb = HistGradientBoostingClassifier(
    learning_rate=0.05, max_iter=2000,
    early_stopping=True,
    class_weight="balanced", random_state=42)
gb.fit(X_train, y_train)
# random validation split: fine here; for
# fraud, validate on later-in-time data
