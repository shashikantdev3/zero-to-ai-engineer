"""Zero to AI Engineer · Python · Interview Quiz
Slide: Flatten a nested dictionary
Run: python 03_flatten_a_nested_dictionary.py
"""
def flatten(d, parent=""):
    out = {}
    for k, v in d.items():
        key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict) and v:
            out.update(flatten(v, key))
        else:
            out[key] = v
    return out
cfg = {"a": {"b": 1, "c": {}}, "d": [1, 2]}
print(flatten(cfg))
