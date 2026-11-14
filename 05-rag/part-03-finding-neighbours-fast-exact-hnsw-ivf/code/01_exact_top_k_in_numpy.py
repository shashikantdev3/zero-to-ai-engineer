"""Zero to AI Engineer · RAG and Vector Search · Part 3 of 26
Slide: Exact top k in NumPy
Run: python 01_exact_top_k_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np

def exact_top_k(matrix, query, k=10):
    # matrix (n, d), query (d,), normalised
    scores = matrix @ query
    # argpartition needs k < n
    if k >= len(scores):
        return np.argsort(-scores)
    idx = np.argpartition(-scores, k)[:k]
    return idx[np.argsort(-scores[idx])]
m = np.eye(4)
print(exact_top_k(m, m[2], k=2))
