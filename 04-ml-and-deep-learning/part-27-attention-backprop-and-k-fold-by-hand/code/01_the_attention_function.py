"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: The attention function
Run: python 01_the_attention_function.py
"""
# Needs: pip install numpy
import numpy as np

def attention(Q, K, V, mask=None):
    s = Q @ K.T / np.sqrt(Q.shape[-1])
    if mask is not None:
        # mask goes before the softmax
        s = np.where(mask, s, -1e9)
    w = np.exp(s - s.max(-1, keepdims=True))
    w /= w.sum(-1, keepdims=True)
    return w @ V
