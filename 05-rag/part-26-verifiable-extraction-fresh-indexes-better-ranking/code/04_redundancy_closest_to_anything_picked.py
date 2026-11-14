"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: Redundancy: closest to anything picked
Run: python 04_redundancy_closest_to_anything_picked.py
"""
# Needs: pip install numpy
import numpy as np

def redundancy(docs, cand, sel):
    # max similarity to anything picked
    if not sel:
        return np.zeros(len(cand))
    sims = docs[cand] @ docs[sel].T
    return sims.max(axis=1)
