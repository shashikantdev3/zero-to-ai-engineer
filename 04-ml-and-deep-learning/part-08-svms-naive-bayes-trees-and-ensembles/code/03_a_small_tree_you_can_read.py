"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 8 of 28
Slide: A small tree you can read
Run: python 03_a_small_tree_you_can_read.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import load_iris
from sklearn.tree import (
    DecisionTreeClassifier, export_text)
X_train, y_train = load_iris(
    return_X_y=True, as_frame=True)
t = DecisionTreeClassifier(
    max_depth=4, min_samples_leaf=50)
t.fit(X_train, y_train)
names = list(X_train.columns)
print(export_text(t, feature_names=names))
