"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: Scaled k-NN in a Pipeline
Run: python 09_scaled_k_nn_in_a_pipeline.py
"""
# Needs: pip install scikit-learn
from sklearn.datasets import (
    make_classification)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import (
    StandardScaler)
from sklearn.neighbors import (
    KNeighborsClassifier)
X_train, y_train = make_classification(
    n_samples=200, random_state=0)
knn = make_pipeline(StandardScaler(),
    KNeighborsClassifier(n_neighbors=15))
knn.fit(X_train, y_train)
