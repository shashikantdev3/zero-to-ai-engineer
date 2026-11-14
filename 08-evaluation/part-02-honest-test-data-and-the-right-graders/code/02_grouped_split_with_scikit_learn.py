"""Zero to AI Engineer · Evaluation · Part 2 of 11
Slide: Grouped split with scikit-learn
Run: python 02_grouped_split_with_scikit_learn.py
"""
# Needs: pip install scikit-learn
from sklearn.model_selection import (
    GroupShuffleSplit)
cases = [{"conversation_id": i // 2, "q": i}
         for i in range(10)]
# group = conversation, incident or user
groups = [c["conversation_id"] for c in cases]
splitter = GroupShuffleSplit(
    n_splits=1, test_size=0.3, random_state=7)
dev_idx, held_idx = next(
    splitter.split(cases, groups=groups))
dev = [cases[i] for i in dev_idx]
held_out = [cases[i] for i in held_idx]
