"""Zero to AI Engineer · LLM Fundamentals · Part 7 of 18
Slide: Building the mask in NumPy
Run: python 01_building_the_mask_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np

n = 4
ones = np.ones((n, n), dtype=bool)
# keep cells above the diagonal
mask = np.triu(ones, k=1)
print(mask.astype(int))
# 1 = blocked (future position)
