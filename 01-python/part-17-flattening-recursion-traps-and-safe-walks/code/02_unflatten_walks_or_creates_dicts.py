"""Zero to AI Engineer · Python · Part 17 of 25
Slide: Unflatten walks or creates dicts
Run: python 02_unflatten_walks_or_creates_dicts.py
"""
def unflatten(flat, sep="."):
    out = {}
    for compound, value in flat.items():
        parts = compound.split(sep)
        node = out
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = value
    return out

print(unflatten({"a.0.b": 1, "a.1.b": 2}))
# {'a': {'0': {'b': 1}, '1': {'b': 2}}}
