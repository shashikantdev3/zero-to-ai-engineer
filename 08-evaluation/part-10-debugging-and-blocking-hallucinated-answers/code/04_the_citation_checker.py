"""Zero to AI Engineer · Evaluation · Part 10 of 11
Slide: The citation checker
Run: python 04_the_citation_checker.py
"""
# --- repeated from 03_normalize_then_check.py so this file runs on its own ---
import re
# example; tune on your data
MIN_QUOTE_CHARS = 20

def norm(s: str) -> str:
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

retrieved = {
    "c1": "Refunds are paid within 14 days."}
claims = [{"text": "Refunds take 14 days.",
           "source_id": "c1", "quote": ""}]

# --- this slide ---
def check_citations(claims, retrieved):
    bad = []
    for c in claims:
        quote = norm(c.get("quote") or "")
        sid = c.get("source_id")
        src = retrieved.get(sid)
        if (src is None
            or len(quote) < MIN_QUOTE_CHARS
            or quote not in norm(src)):
            bad.append(c.get("text", ""))
    return bad
print(check_citations(claims, retrieved))
