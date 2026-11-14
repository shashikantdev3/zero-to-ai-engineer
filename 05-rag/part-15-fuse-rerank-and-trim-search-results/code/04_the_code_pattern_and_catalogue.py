"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: The code pattern and catalogue
Run: python 04_the_code_pattern_and_catalogue.py
"""
import re
# loaded from the product catalogue
CATALOGUE = {"XR4410A", "XR4410B"}
CODE = re.compile(
    r"\b([A-Z]{2})[\s-]?(\d{4})"
    r"(?:[\s-]?([A-Z]))?\b",
    re.IGNORECASE,
)
