"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: Check the first row
Run: python 02_check_the_first_row.py
"""
# Needs: pip install numpy
# --- repeated from 01_the_attention_function.py so this file runs on its own ---
import numpy as np

def attention(Q, K, V, mask=None):
    s = Q @ K.T / np.sqrt(Q.shape[-1])
    if mask is not None:
        # mask goes before the softmax
        s = np.where(mask, s, -1e9)
    w = np.exp(s - s.max(-1, keepdims=True))
    w /= w.sum(-1, keepdims=True)
    return w @ V

# --- this slide ---
rng = np.random.default_rng(0)
Q, K, V = rng.normal(size=(3, 4, 8))
n = len(Q)
# lower triangle: each token sees the past
mask = np.tril(np.ones((n, n), dtype=bool))
out = attention(Q, K, V, mask)
assert np.allclose(out[0], V[0])
print(out.shape)
