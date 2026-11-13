"""Zero to AI Engineer · LLM Fundamentals · Part 10 of 18
Slide: Cross-attention in NumPy
Run: python 03_cross_attention_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np
def cross_attention(Y, H, Wq, Wk, Wv):
    Q = Y @ Wq  # from the decoder
    # from the encoder, computed once
    K = H @ Wk
    V = H @ Wv
    # (m, n), no causal mask on the source
    s = Q @ K.T / np.sqrt(K.shape[-1])
    s -= s.max(axis=-1, keepdims=True)
    w = np.exp(s)
    w /= w.sum(axis=-1, keepdims=True)
    return w @ V
