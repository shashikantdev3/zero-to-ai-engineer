"""Zero to AI Engineer · RAG and Vector Search · Part 1 of 26
Slide: Cosine Similarity in NumPy
Run: python 05_cosine_similarity_in_numpy.py
"""
# Needs: pip install numpy
import numpy as np

def cosine(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    denom = (np.linalg.norm(a)
             * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(a @ b / denom)

print(cosine([1, 0], [2, 0]))
