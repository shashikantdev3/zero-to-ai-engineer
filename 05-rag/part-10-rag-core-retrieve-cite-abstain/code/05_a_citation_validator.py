"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: A citation validator
Run: python 05_a_citation_validator.py
"""
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
