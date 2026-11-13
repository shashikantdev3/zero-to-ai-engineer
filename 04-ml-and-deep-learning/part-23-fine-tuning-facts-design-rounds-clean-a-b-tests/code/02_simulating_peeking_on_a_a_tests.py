"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 23 of 28
Slide: Simulating peeking on A/A tests
Run: python 02_simulating_peeking_on_a_a_tests.py
"""
# Needs: pip install numpy scipy
import numpy as np
from scipy import stats
rng = np.random.default_rng(0)
hits = 0
# A/A tests: no real effect
for _ in range(2000):
    a, b = rng.normal(size=(2, 5000))
    ps = [stats.ttest_ind(a[:n], b[:n]).pvalue
          for n in range(500, 5001, 500)]
    hits += min(ps) < 0.05
# well above 0.05 with ten peeks
print(hits / 2000)
