"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 8 of 28
Slide: A random forest with OOB score
Run: python 05_a_random_forest_with_oob_score.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import load_wine
from sklearn.ensemble import (
    RandomForestClassifier)
X_train, y_train = load_wine(return_X_y=True)
rf = RandomForestClassifier(
    n_estimators=500, min_samples_leaf=5,
    class_weight="balanced", oob_score=True,
    n_jobs=-1, random_state=42)
rf.fit(X_train, y_train)
print(rf.oob_score_)
