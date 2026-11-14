"""Zero to AI Engineer · RAG and Vector Search · Part 15 of 26
Slide: Normalise and validate codes
Run: python 05_normalise_and_validate_codes.py
"""
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
