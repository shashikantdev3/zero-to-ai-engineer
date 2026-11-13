"""Zero to AI Engineer · Python · Part 24 of 25
Slide: Counting emails in code
Run: python 04_counting_emails_in_code.py
"""
import re
from collections import Counter
EMAIL = re.compile(
    r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
def count_emails(path: str) -> Counter:
    c: Counter = Counter()
    with open(path, encoding="utf-8",
              errors="replace") as f:
        for line in f:
            found = EMAIL.findall(line)
            c.update(m.lower() for m in found)
    return c
