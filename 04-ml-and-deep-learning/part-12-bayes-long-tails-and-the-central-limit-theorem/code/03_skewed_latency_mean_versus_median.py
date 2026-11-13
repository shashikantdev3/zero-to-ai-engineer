"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 12 of 28
Slide: Skewed latency, mean versus median
Run: python 03_skewed_latency_mean_versus_median.py
"""
# Needs: pip install numpy
import numpy as np
rng = np.random.default_rng(0)
# skewed latency in milliseconds
lat = rng.lognormal(mean=3.9, sigma=0.8,
                    size=100_000)
print(lat.mean())
# median, p95, p99
print(np.percentile(lat, [50, 95, 99]))
