"""Zero to AI Engineer · LLM Fundamentals · Part 10 of 18
Slide: Combining causal and padding masks
Run: python 01_combining_causal_and_padding_masks.py
"""
# Needs: pip install numpy
import numpy as np

n = 4
scores = np.random.randn(n, n)
causal = np.tril(np.ones((n, n), dtype=bool))
# last token is padding
pad = np.array([True, True, True, False])
# block attention TO padding
mask = causal & pad[None, :]
# finite, so no NaN on empty rows
scores = np.where(mask, scores, -1e9)
