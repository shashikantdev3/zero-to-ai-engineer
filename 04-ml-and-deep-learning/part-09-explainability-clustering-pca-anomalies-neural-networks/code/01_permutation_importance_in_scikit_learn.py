"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Slide: Permutation importance in scikit-learn
Run: python 01_permutation_importance_in_scikit_learn.py
"""
# Needs: pip install scikit-learn
from sklearn import datasets, ensemble
from sklearn import inspection
X, y = datasets.make_classification(
    n_samples=400, random_state=42)
X_tr, X_val = X[:300], X[300:]
y_tr, y_val = y[:300], y[300:]
gb = ensemble.GradientBoostingClassifier()
gb.fit(X_tr, y_tr)
r = inspection.permutation_importance(
    gb, X_val, y_val,
    scoring="average_precision",
    n_repeats=10, random_state=42)
