"""Zero to AI Engineer · Python · Part 1 of 25
Slide: Four ways to build collections
Run: python 05_four_ways_to_build_collections.py
"""
chunks = ["alpha beta", "", "gamma"]
non_empty = [c for c in chunks if c]
by_len = {c: len(c) for c in non_empty}
words = {w for c in chunks for w in c.split()}   # outer loop first
total = sum(len(c) for c in chunks)              # lazy, no list built
