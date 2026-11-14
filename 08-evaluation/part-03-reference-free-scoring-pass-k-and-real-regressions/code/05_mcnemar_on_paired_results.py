"""Zero to AI Engineer · Evaluation · Part 3 of 11
Slide: McNemar on paired results
Run: python 05_mcnemar_on_paired_results.py
"""
# Needs: pip install scipy
from scipy.stats import binomtest
def mcnemar_exact(old, new):
    # compare TWO versions on same case IDs
    assert set(old) == set(new)
    pairs = [(old[c], new[c]) for c in old]
    broke = pairs.count((True, False))
    fixed = pairs.count((False, True))
    n = broke + fixed
    if n == 0:
        return broke, fixed, 1.0
    p = binomtest(fixed, n, 0.5).pvalue
    return broke, fixed, p
