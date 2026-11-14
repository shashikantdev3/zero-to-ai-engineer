"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: Testing the normaliser
Run: python 06_testing_the_normaliser.py
"""
# --- repeated from 04_the_code_pattern_and_catalogue.py, 05_normalise_and_validate_codes.py so this file runs on its own ---
import re
# loaded from the product catalogue
CATALOGUE = {"XR4410A", "XR4410B"}
CODE = re.compile(
    r"\b([A-Z]{2})[\s-]?(\d{4})"
    r"(?:[\s-]?([A-Z]))?\b",
    re.IGNORECASE,
)

def normalise_codes(text):
    found = set()
    for p, d, s in CODE.findall(text):
        full = f"{p}{d}{s}".upper()
        short = f"{p}{d}".upper()
        for cand in (full, short):
            # only real catalogue codes count
            if cand in CATALOGUE:
                found.add(cand)
                break
    return found

# --- this slide ---
t = "Fault on xr 4410 b and XR-4410A"
found = normalise_codes(t)
assert found == {"XR4410B", "XR4410A"}
none = normalise_codes("policy in 2026")
assert none == set()
