"""Zero to AI Engineer · LLM Fundamentals · Part 6 of 18
Slide: Self-attention in NumPy
Run: python 01_self_attention_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np
def attn(X, Wq, Wk, Wv, causal=True):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    s = Q @ K.T / np.sqrt(K.shape[-1])
    if causal:
        n = s.shape[0]
        m = np.triu(np.ones((n, n), bool), k=1)
        s = np.where(m, -np.inf, s)
    s -= s.max(axis=-1, keepdims=True)
    w = np.exp(s)
    w /= w.sum(axis=-1, keepdims=True)
    return w @ V
