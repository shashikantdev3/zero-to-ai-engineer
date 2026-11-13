"""Zero to AI Engineer · Python · Part 16 of 25
Slide: A stable key with hashlib
Run: python 01_a_stable_key_with_hashlib.py
"""
import hashlib
seen: set[str] = set()
def doc_key(text: str) -> str:
    data = text.encode("utf-8")
    # stable across runs
    return hashlib.sha256(data).hexdigest()
for t in ["a", "a", "b"]:
    k = doc_key(t)
    if k in seen:  # O(1) average
        continue
    seen.add(k)
print(len(seen))  # 2
