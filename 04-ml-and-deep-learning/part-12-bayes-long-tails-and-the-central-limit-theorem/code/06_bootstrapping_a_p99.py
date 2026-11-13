"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 12 of 28
Slide: Bootstrapping a p99
Run: python 06_bootstrapping_a_p99.py
"""
# Needs: pip install numpy
# --- repeated from 05_averaging_skewed_data.py so this file runs on its own ---
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

# --- this slide ---
# continues: bootstrap the p99
flat = x.ravel()
boot = []
for _ in range(100):
    resample = rng.choice(flat, flat.size)
    boot.append(np.percentile(resample, 99))
print(np.std(boot))
