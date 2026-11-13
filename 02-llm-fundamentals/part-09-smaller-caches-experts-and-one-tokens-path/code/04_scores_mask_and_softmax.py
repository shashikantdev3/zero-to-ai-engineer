"""Zero to AI Engineer · LLM Fundamentals · Part 9 of 18
Slide: Scores, mask, and softmax
Run: python 04_scores_mask_and_softmax.py
"""
# Needs: pip install numpy
import numpy as np
def attend(Q, K, V, causal=True):
    dk, n = Q.shape[-1], Q.shape[-2]
    s = Q @ K.swapaxes(-1, -2) / np.sqrt(dk)
    if causal:
        m = np.ones((n, n), dtype=bool)
        keep = np.tril(m)
        s = np.where(keep, s, -1e9)
    s = s - s.max(axis=-1, keepdims=True)
    w = np.exp(s)
    w = w / w.sum(axis=-1, keepdims=True)
    return w @ V
