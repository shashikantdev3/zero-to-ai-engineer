"""Zero to AI Engineer · Python · Part 23 of 25
Slide: normalise and normalise_code
Run: python 01_normalise_and_normalise_code.py
"""
import re
import unicodedata as ud
_WS = re.compile(r"\s+")
def normalise(s: str) -> str:
    # NFKC, casefold, then NFKC again
    s = ud.normalize("NFKC", s).casefold()
    s = ud.normalize("NFKC", s)
    return _WS.sub(" ", s).strip()
def normalise_code(s: str) -> str:
    t = normalise(s)
    return re.sub(r"[^0-9a-z]", "", t)
