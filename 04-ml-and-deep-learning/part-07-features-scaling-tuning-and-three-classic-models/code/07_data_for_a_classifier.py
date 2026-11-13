"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: Data for a Classifier
Run: python 07_data_for_a_classifier.py
"""
# Needs: pip install scikit-learn
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
