"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: A Pipeline to Tune
Run: python 04_a_pipeline_to_tune.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import (
    make_classification)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import (
    StandardScaler)
from sklearn.linear_model import (
    LogisticRegression)
X_train, y_train = make_classification(
    n_samples=300, weights=[0.9],
    random_state=0)
pipe = make_pipeline(StandardScaler(),
    LogisticRegression(max_iter=2000))
