"""Zero to AI Engineer · LLM Fundamentals · Part 11 of 18
Slide: A sliding-window mask is a band
Run: python 04_a_sliding_window_mask_is_a_band.py
"""
# Needs: pip install numpy
import numpy as np


def sliding_mask(n, w):
    i = np.arange(n)[:, None]
    j = np.arange(n)[None, :]
    # causal and within the last w tokens
    return (j <= i) & (j > i - w)


print(sliding_mask(5, 2).astype(int))
