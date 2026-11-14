"""Zero to AI Engineer · RAG and Vector Search · Part 8 of 26
Slide: Exact baseline and recall
Run: python 05_exact_baseline_and_recall.py
"""
# Needs: pip install numpy
import numpy as np
K, TARGET = 10, 0.95
def exact_top_k(xb, queries, k):
    # brute-force baseline, 10k sample
    return [np.argsort(-(xb @ q))[:k]
            for q in queries]
def recall_at_k(ids, exact, k):
    s = [len(set(a) & set(e)) / k
         for a, e in zip(ids, exact)]
    return float(np.mean(s))
