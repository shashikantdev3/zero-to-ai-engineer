"""Zero to AI Engineer · Python · Part 24 of 25
Slide: Estimating Jaccard
Run: python 03_estimating_jaccard.py
"""
# --- repeated from 01_shingles_in_code.py, 02_minimum_hashes_in_code.py so this file runs on its own ---
import hashlib
def shingles(text: str,
             k: int = 5) -> set[str]:
    words = text.split()
    if not words:
        return set()
    n = max(1, len(words) - k + 1)
    return {" ".join(words[i:i + k])
            for i in range(n)}

import hashlib
def _h(s: str, seed: int) -> int:
    salt = seed.to_bytes(16, "little")
    d = hashlib.blake2b(
        s.encode("utf-8"),
        digest_size=8, salt=salt)
    return int.from_bytes(d.digest(), "big")
def minhash(sh: set[str], n: int = 128):
    if not sh:
        return None
    return [min(_h(s, i) for s in sh)
            for i in range(n)]

# --- this slide ---
def est_jaccard(a, b) -> float:
    # empty doc: policy choice, not similar
    if a is None or b is None:
        return 0.0
    same = sum(x == y for x, y
               in zip(a, b, strict=True))
    return same / len(a)
t = "the leave policy allows twenty days"
t += " of paid leave per year"
a = minhash(shingles(t))
b = minhash(shingles(t + " footer v2"))
print(round(est_jaccard(a, b), 2))
