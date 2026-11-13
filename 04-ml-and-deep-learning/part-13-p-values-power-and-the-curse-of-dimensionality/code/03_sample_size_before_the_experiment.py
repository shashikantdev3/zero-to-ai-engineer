"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 13 of 28
Slide: Sample size before the experiment
Run: python 03_sample_size_before_the_experiment.py
"""
# Needs: pip install statsmodels
from statsmodels.stats import power
from statsmodels.stats import proportion
# detect a lift from 10% to 11% conversion
h = proportion.proportion_effectsize(
    0.11, 0.10)
n = power.NormalIndPower().solve_power(
    effect_size=h, alpha=0.05, power=0.8)
print("users per arm:", round(n))
