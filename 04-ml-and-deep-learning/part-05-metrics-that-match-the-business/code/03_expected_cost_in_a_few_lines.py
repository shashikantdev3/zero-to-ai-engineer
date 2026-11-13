"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 5 of 28
Slide: Expected cost in a few lines
Run: python 03_expected_cost_in_a_few_lines.py
"""
# Needs: pip install numpy
import numpy as np
y = np.array([1, 0, 1, 0, 0])
pred = np.array([0, 1, 1, 0, 1])
amount = np.array([900.0, 20, 80, 30, 10])
def expected_cost(y, pred, amount,
                  fp_cost=50.0):
    fn = (y == 1) & (pred == 0)
    fp = (y == 0) & (pred == 1)
    return amount[fn].sum() + fp_cost * fp.sum()
print(expected_cost(y, pred, amount))
