"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Slide: Merging the Pair
Run: python 05_merging_the_pair.py
"""
def merge(words, pair):
    out = []
    for w in words:
        i, new = 0, []
        while i < len(w):
            hit = tuple(w[i:i + 2]) == pair
            n = 2 if hit else 1
            new.append("".join(w[i:i + n]))
            i += n
        out.append(tuple(new))
    return out
