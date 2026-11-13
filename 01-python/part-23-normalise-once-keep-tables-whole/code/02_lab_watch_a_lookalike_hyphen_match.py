"""Zero to AI Engineer · Python · Part 23 of 25
Follow-along lab: Watch a lookalike hyphen match
Run: python 02_lab_watch_a_lookalike_hyphen_match.py
"""
import re
import unicodedata as ud
def norm(s: str) -> str:
    s = ud.normalize("NFKC", s).casefold()
    s = ud.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()
def code(s: str) -> str:
    return re.sub(r"[^0-9a-z]", "", norm(s))
a = "XR\u20114410B"
b = "xr 4410 b"
print("lower:", a.lower() == b.lower())
print("code:", code(a) == code(b))
print("value:", code(a))
print("digit:", norm("\uff14\uff14") == "44")
