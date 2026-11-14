"""Zero to AI Engineer · Evaluation · Part 10 of 11
Slide: Normalize, then check
Run: python 03_normalize_then_check.py
"""
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
