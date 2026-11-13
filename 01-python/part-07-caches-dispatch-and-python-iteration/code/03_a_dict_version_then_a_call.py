"""Zero to AI Engineer · Python · Part 7 of 25
Slide: A dict version, then a call
Run: python 03_a_dict_version_then_a_call.py
"""
# --- repeated from 02_a_default_and_a_list_version.py so this file runs on its own ---
from functools import singledispatch

@singledispatch
def render(obj) -> str:
    return repr(obj)

@render.register
def _(obj: list) -> str:
    inner = ", ".join(render(x) for x in obj)
    return "[" + inner + "]"

# --- this slide ---
# continues from the previous slide
@render.register
def _(obj: dict) -> str:
    inner = ", ".join(
        f"{k}={render(v)}"
        for k, v in obj.items()
    )
    return "{" + inner + "}"

data = {"ids": [1, 2], "ok": True}
print(render(data))
# {ids=[1, 2], ok=True}
