"""Zero to AI Engineer · Python · Interview Quiz
Slide: Recurse into lists only
Run: python 02_recurse_into_lists_only.py
"""
def flat(xs):
    for x in xs:
        if isinstance(x, list):
            yield from flat(x)
        else:
            yield x
print(list(flat([1, [2, [3, "ab"]]])))
