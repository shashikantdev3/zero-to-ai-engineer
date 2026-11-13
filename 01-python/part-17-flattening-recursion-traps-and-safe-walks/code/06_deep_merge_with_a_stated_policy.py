"""Zero to AI Engineer · Python · Part 17 of 25
Slide: Deep merge with a stated policy
Run: python 06_deep_merge_with_a_stated_policy.py
"""
def deep_merge(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, v in b.items():
        left = isinstance(out.get(k), dict)
        if left and isinstance(v, dict):
            out[k] = deep_merge(out[k], v)
        else:  # policy: b wins
            out[k] = v
    return out
a = {"m": {"x": 1}, "t": 1}
b = {"m": {"y": 2}, "t": 2}
print(deep_merge(a, b))
