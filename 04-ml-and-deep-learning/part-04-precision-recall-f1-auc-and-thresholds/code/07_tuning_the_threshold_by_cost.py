"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Slide: Tuning the Threshold by Cost
Run: python 07_tuning_the_threshold_by_cost.py
"""
# Needs: pip install numpy scikit-learn
# --- repeated from 06_a_cost_function_for_thresholds.py so this file runs on its own ---
import numpy as np
from sklearn.metrics import make_scorer

# illustrative costs: agree with the business
def neg_expected_cost(y, pred, fn_cost=5000.0,
                      fp_cost=50.0):
    y, pred = np.asarray(y), np.asarray(pred)
    fn = ((y == 1) & (pred == 0)).sum()
    fp = ((y == 0) & (pred == 1)).sum()
    return -(fn_cost * fn + fp_cost * fp)

scorer = make_scorer(neg_expected_cost)

# --- this slide ---
from sklearn import datasets, linear_model
from sklearn import model_selection as ms

X, y = datasets.make_classification(
    n_samples=2000, weights=[0.97],
    random_state=0)
base_model = linear_model.LogisticRegression()
clf = ms.TunedThresholdClassifierCV(
    base_model, scoring=scorer,
    cv=ms.TimeSeriesSplit(n_splits=5))
clf.fit(X, y)
print(clf.best_threshold_)
