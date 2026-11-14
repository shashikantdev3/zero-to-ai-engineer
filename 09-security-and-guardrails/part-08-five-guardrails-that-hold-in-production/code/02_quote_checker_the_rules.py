"""Zero to AI Engineer · Security and Guardrails · Part 8 of 11
Slide: Quote checker: the rules
Run: python 02_quote_checker_the_rules.py
"""
import re
MIN_WORDS = 5
# the quote must be rare in the source
MAX_OCCURRENCES = 2
# e.g. ORA-00942 or 0x80070005
ID_PATTERN = re.compile(
    r"^[A-Z]{2,}[-_]?\d{2,}$"
    r"|^0x[0-9A-Fa-f]+$")

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()
