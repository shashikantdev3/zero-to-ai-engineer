"""Zero to AI Engineer · Python · Part 11 of 25
Slide: suppress and ExitStack
Run: python 02_suppress_and_exitstack.py
"""
from contextlib import suppress, ExitStack

with suppress(FileNotFoundError):
    open("missing.txt")

paths = ["a.txt", "b.txt"]
with ExitStack() as stack:
    files = [
        stack.enter_context(open(p, "w"))
        for p in paths
    ]
