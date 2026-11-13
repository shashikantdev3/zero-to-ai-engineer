"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 4 of 28
Slide: A Cost Function for Thresholds
Run: python 06_a_cost_function_for_thresholds.py
"""
# Needs: pip install numpy scikit-learn
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
