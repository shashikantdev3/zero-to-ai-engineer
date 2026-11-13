"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 12 of 28
Slide: Averaging skewed data
Run: python 05_averaging_skewed_data.py
"""
# Needs: pip install numpy
import numpy as np
rng = np.random.default_rng(0)
# skewed raw data: 10,000 samples of 50
x = rng.exponential(scale=100,
                    size=(10_000, 50))
# 10,000 sample means: close to normal
means = x.mean(axis=1)
print(means.mean(), means.std())
# standard error: sigma over root n
print(x.std() / 50 ** 0.5)
