"""Zero to AI Engineer · Python · Part 24 of 25
Slide: Minimum hashes in code
Run: python 02_minimum_hashes_in_code.py
"""
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
