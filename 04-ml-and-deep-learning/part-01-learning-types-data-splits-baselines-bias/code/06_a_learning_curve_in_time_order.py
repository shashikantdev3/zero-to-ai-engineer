"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 1 of 28
Slide: A learning curve, in time order
Run: python 06_a_learning_curve_in_time_order.py
"""
# Needs: pip install scikit-learn
from sklearn.model_selection import (
    learning_curve, TimeSeriesSplit)
from sklearn.linear_model import (
    LogisticRegression)
X = [[i % 7, i % 5] for i in range(300)]
y = [int(i % 7 == 0) for i in range(300)]
sizes, train_s, val_s = learning_curve(
    LogisticRegression(), X, y,
    cv=TimeSeriesSplit(n_splits=5),
    scoring="average_precision")
print(train_s.mean(axis=1))
print(val_s.mean(axis=1))
