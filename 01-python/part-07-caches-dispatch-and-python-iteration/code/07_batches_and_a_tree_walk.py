"""Zero to AI Engineer · Python · Part 7 of 25
Slide: Batches and a tree walk
Run: python 07_batches_and_a_tree_walk.py
"""
from itertools import islice

def batches(it, n):
    it = iter(it)
    while (batch := list(islice(it, n))):
        # itertools.batched(it, n) on 3.12+
        yield batch

def walk(tree):
    yield tree["id"]
    for child in tree.get("children", []):
        yield from walk(child)
