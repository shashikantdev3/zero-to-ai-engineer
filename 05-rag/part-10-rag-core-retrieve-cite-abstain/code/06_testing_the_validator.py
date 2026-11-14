"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: Testing the validator
Run: python 06_testing_the_validator.py
"""
# --- repeated from 05_a_citation_validator.py so this file runs on its own ---
import re
REFUSAL = "I do not know. Open a ticket?"
# matches ids like leave-policy-2026#s3-c2
CITE = re.compile(
    r"\[([A-Za-z0-9._-]+#[A-Za-z0-9_-]+)\]")

def validate_citations(text, top_ids):
    cited = set(CITE.findall(text))
    if not cited or not cited <= set(top_ids):
        return REFUSAL
    return text

# --- this slide ---
top_ids = ["leave-policy-2026#s3-c2"]
good = "25 days [leave-policy-2026#s3-c2]."
fake = "30 days [travel-2024#s1-c1]."
print(validate_citations(good, top_ids))
print(validate_citations(fake, top_ids))
print(validate_citations("25 days.", top_ids))
