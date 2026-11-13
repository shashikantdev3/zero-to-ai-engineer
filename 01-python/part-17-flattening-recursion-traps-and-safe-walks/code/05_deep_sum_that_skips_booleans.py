"""Zero to AI Engineer · Python · Part 17 of 25
Slide: Deep sum that skips booleans
Run: python 05_deep_sum_that_skips_booleans.py
"""
def deep_sum(obj) -> float:
    if isinstance(obj, bool):
        return 0
    if isinstance(obj, (int, float)):
        return obj
    if isinstance(obj, dict):
        obj = list(obj.values())
    if isinstance(obj, list):
        return sum(deep_sum(v) for v in obj)
    return 0

print(deep_sum({"x": 1, "ok": True}))  # 1
