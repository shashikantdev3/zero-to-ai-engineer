"""Zero to AI Engineer · Python · Part 7 of 25
Slide: A default and a list version
Run: python 02_a_default_and_a_list_version.py
"""
from functools import singledispatch

@singledispatch
def render(obj) -> str:
    return repr(obj)

@render.register
def _(obj: list) -> str:
    inner = ", ".join(render(x) for x in obj)
    return "[" + inner + "]"
