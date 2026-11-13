"""Zero to AI Engineer · Python · Part 24 of 25
Slide: Shingles in code
Run: python 01_shingles_in_code.py
"""
import hashlib
def shingles(text: str,
             k: int = 5) -> set[str]:
    words = text.split()
    if not words:
        return set()
    n = max(1, len(words) - k + 1)
    return {" ".join(words[i:i + k])
            for i in range(n)}
