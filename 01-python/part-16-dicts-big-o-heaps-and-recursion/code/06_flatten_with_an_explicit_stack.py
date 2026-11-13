"""Zero to AI Engineer · Python · Part 16 of 25
Slide: Flatten with an explicit stack
Run: python 06_flatten_with_an_explicit_stack.py
"""
def flatten_iter(d, sep="."):
    out, stack = {}, [("", d)]
    while stack:
        parent, cur = stack.pop()
        pre = parent + sep if parent else ""
        for k, v in cur.items():
            key = pre + str(k)
            if isinstance(v, dict) and v:
                stack.append((key, v))
            else:
                out[key] = v
    return out
