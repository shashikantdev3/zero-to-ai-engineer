"""Zero to AI Engineer · Python · Part 17 of 25
Slide: A walk with a cycle guard
Run: python 07_a_walk_with_a_cycle_guard.py
"""
def walk(obj, seen=frozenset()):
    if id(obj) in seen: return "<cycle>"
    if isinstance(obj, (dict, list)):
        seen = seen | {id(obj)}
    if isinstance(obj, dict):
        return {k: walk(v, seen)
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk(v, seen) for v in obj]
    return obj
d = {"x": 1}; d["self"] = d
print(walk(d))
