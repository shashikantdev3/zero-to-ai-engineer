"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Mean versus percentiles
Run: python 10_mean_versus_percentiles.py
"""
# Needs: pip install numpy
import numpy as np

latencies_s = [1.1, 1.3, 0.9, 1.2, 1.0,
               1.4, 1.1, 9.2, 1.2, 8.7]
lat = np.array(latencies_s)
print(lat.mean())
print(np.percentile(lat, 50))
print(np.percentile(lat, 95))
print(np.percentile(lat, 99))
