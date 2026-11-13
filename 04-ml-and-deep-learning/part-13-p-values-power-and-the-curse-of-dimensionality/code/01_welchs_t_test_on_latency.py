"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 13 of 28
Slide: Welch's t-test on latency
Run: python 01_welchs_t_test_on_latency.py
"""
# Needs: pip install numpy scipy
from scipy import stats
import numpy as np
new = [101, 98, 95, 99, 97, 96, 100, 94]
old = [108, 104, 110, 103, 107, 105, 109, 106]
# Welch's t-test: unequal variances allowed
res = stats.ttest_ind(
    new, old, equal_var=False)
diff = np.mean(new) - np.mean(old)
ci = res.confidence_interval(0.95)
print("p:", res.pvalue)
print("difference:", diff)
print("95% CI:", ci.low, ci.high)
