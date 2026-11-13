"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 26 of 28
Slide: top_k with argpartition
Run: python 01_top_k_with_argpartition.py
"""
# Needs: pip install numpy
import numpy as np
def top_k(query, corpus, k=5):
    eps = 1e-10
    q = query / (np.linalg.norm(query) + eps)
    nc = np.linalg.norm(corpus, axis=1,
                        keepdims=True)
    s = (corpus / (nc + eps)) @ q
    k = min(k, len(s))
    if k == 0: return []
    idx = np.argpartition(-s, k - 1)[:k]
    out = [(int(i), float(s[i])) for i in idx]
    return sorted(out, key=lambda t: -t[1])
