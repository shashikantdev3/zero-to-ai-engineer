"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 24 of 28
Slide: Correcting Many p-values
Run: python 04_correcting_many_p_values.py
"""
# Needs: pip install statsmodels
from statsmodels.stats.multitest import (
    multipletests,
)

p_values = [0.01, 0.04, 0.03, 0.20, 0.50]
reject, p_adj, _, _ = multipletests(
    p_values, alpha=0.05, method="fdr_bh"
)
print(reject)
print(p_adj)
