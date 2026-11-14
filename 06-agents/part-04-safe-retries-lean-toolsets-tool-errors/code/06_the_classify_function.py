"""Zero to AI Engineer · Agents and Tools · Part 4 of 26
Slide: The classify function
Run: python 06_the_classify_function.py
"""
# --- repeated from 05_naming_the_four_classes.py so this file runs on its own ---
from enum import Enum

class Kind(Enum):
    TRANSIENT = "transient"
    SEMANTIC = "semantic"
    PERMANENT = "permanent"
    SYSTEMIC = "systemic"

# None stands for a timeout
RETRY = (408, 429, 502, 503, 504, None)

# --- this slide ---
def classify(status, breaker_open, bad_args):
    if breaker_open:
        return Kind.SYSTEMIC
    if bad_args:
        return Kind.SEMANTIC
    if status in RETRY:
        return Kind.TRANSIENT
    # 400 after validation, 403, 404
    return Kind.PERMANENT

print(classify(503, False, False))
print(classify(404, False, False))
