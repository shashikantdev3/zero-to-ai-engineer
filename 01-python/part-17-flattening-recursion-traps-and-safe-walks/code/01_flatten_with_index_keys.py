"""Zero to AI Engineer · Python · Part 17 of 25
Slide: Flatten with index keys
Run: python 01_flatten_with_index_keys.py
"""
def flatten(obj, parent="", sep="."):
    if parent == "" and obj in ({}, []):
        return {}
    if isinstance(obj, list) and obj:
        obj = dict(enumerate(obj))
    if not (isinstance(obj, dict) and obj):
        return {parent: obj}
    p = parent + sep if parent else ""
    out = {}
    for k, v in obj.items():
        out |= flatten(v, f"{p}{k}", sep)
    return out
