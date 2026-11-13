"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 27 of 28
Slide: k-fold index generator
Run: python 05_k_fold_index_generator.py
"""
# Needs: pip install numpy
import numpy as np

def kfold_indices(n, k=5, seed=0):
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    folds = np.array_split(perm, k)
    for i in range(k):
        rest = folds[:i] + folds[i + 1:]
        yield np.concatenate(rest), folds[i]

for tr, va in kfold_indices(11, k=3):
    print(len(tr), len(va))
