"""Zero to AI Engineer · Evaluation · Part 3 of 11
Slide: The unbiased pass@k estimator
Run: python 03_the_unbiased_pass_k_estimator.py
"""
from math import comb

def pass_at_k(n: int, c: int, k: int):
    # unbiased estimator, Chen et al. 2021
    # n samples, c correct, n >= k
    if n - c < k:
        return 1.0
    return 1.0 - comb(n - c, k) / comb(n, k)

print(pass_at_k(n=10, c=3, k=1))
print(pass_at_k(n=10, c=3, k=5))
