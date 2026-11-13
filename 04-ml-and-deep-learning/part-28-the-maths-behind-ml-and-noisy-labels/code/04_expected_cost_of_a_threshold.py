"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 28 of 28
Slide: Expected Cost of a Threshold
Run: python 04_expected_cost_of_a_threshold.py
"""
# expected cost per case of a threshold,
# given validation counts
fp, fn, n = 120, 15, 10_000
# illustrative costs
cost_fp, cost_fn = 50, 2_000
total = fp * cost_fp + fn * cost_fn
expected_cost = total / n
print(expected_cost)
