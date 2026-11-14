"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: A check is just a function
Run: python 01_a_check_is_just_a_function.py
"""
from typing import Callable

# a check returns (ok, reason)
Check = Callable[[str], tuple[bool, str]]

def first_fail(checks: list[Check], text):
    for check in checks:
        ok, reason = check(text)
        if not ok:
            return reason
    return None
