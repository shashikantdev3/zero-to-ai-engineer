"""Zero to AI Engineer · Security and Guardrails · Part 3 of 11
Slide: Check the hash before loading
Run: python 02_check_the_hash_before_loading.py
"""
import hashlib
# bytes we downloaded (a stand-in file)
data = b"model weights v1"
# hash pinned in our lockfile
PINNED = hashlib.sha256(data).hexdigest()

def verify(blob: bytes) -> bool:
    digest = hashlib.sha256(blob).hexdigest()
    return digest == PINNED

print(verify(data))
print(verify(b"model weights v1 + code"))
