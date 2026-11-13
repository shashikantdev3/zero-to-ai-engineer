"""Zero to AI Engineer · Python · Part 16 of 25
Slide: Flatten, the recursive way
Run: python 05_flatten_the_recursive_way.py
"""
def flatten(d, parent="", sep="."):
    out = {}
    for k, v in d.items():
        key = str(k)
        if parent:
            key = f"{parent}{sep}{k}"
        if isinstance(v, dict) and v:
            out.update(flatten(v, key, sep))
        else:
            # leaf, or empty dict kept as-is
            out[key] = v
    return out
