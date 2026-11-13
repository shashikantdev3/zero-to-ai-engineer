"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 7 of 28
Slide: Random Search with Time Splits
Run: python 05_random_search_with_time_splits.py
"""
# Needs: pip install scipy scikit-learn
# --- repeated from 04_a_pipeline_to_tune.py so this file runs on its own ---
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

# --- this slide ---
from scipy.stats import loguniform
from sklearn.model_selection import (
    RandomizedSearchCV, TimeSeriesSplit)
grid = {"logisticregression__C":
        loguniform(1e-3, 1e2)}
search = RandomizedSearchCV(
    pipe, grid, n_iter=30,
    cv=TimeSeriesSplit(n_splits=5),
    scoring="average_precision",
    random_state=0)
search.fit(X_train, y_train)
print(search.best_params_)
