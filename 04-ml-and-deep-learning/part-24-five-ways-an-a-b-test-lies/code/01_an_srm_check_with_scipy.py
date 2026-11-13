"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 24 of 28
Slide: An SRM Check With SciPy
Run: python 01_an_srm_check_with_scipy.py
"""
# Needs: pip install scipy
from scipy.stats import chisquare

n_a, n_b = 501_234, 498_766
total = n_a + n_b
expected = [total / 2] * 2
res = chisquare([n_a, n_b],
                f_exp=expected)
p = res.pvalue
srm = p < 0.0005
print(p, srm)
