"""Zero to AI Engineer · Evaluation · Part 1 of 11
Slide: Redact the query first
Run: python 02_redact_the_query_first.py
"""
import json, re

EMAIL = re.compile(
    r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\+?\d[\d\s-]{8,}\d")

def redact(text: str) -> str:
    # minimal; use a real PII service in prod
    text = EMAIL.sub("[EMAIL]", text)
    return PHONE.sub("[PHONE]", text)
