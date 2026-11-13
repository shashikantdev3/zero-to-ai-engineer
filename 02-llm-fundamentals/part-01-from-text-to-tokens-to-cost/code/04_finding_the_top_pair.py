"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Slide: Finding the Top Pair
Run: python 04_finding_the_top_pair.py
"""
from collections import Counter

def most_frequent_pair(words):
    # words: list of tuples of symbols
    pairs = Counter()
    for w in words:
        pairs.update(zip(w, w[1:]))
    return pairs.most_common(1)[0][0]
