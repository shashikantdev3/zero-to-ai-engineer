"""Zero to AI Engineer · LLM Fundamentals · Part 7 of 18
Slide: Multi-head attention in NumPy
Run: python 03_multi_head_attention_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np
def self_attention(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    s = Q @ K.T / np.sqrt(K.shape[-1])
    w = np.exp(s - s.max(-1, keepdims=True))
    return w / w.sum(-1, keepdims=True) @ V

def multi_head(X, heads, Wo):
    # heads: list of (Wq, Wk, Wv)
    outs = [self_attention(X, *h)
            for h in heads]
    return np.concatenate(outs, axis=-1) @ Wo
