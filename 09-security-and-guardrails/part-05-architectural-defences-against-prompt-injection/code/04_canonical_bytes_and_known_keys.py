"""Zero to AI Engineer · Security and Guardrails · Part 5 of 11
Slide: Canonical bytes and known keys
Run: python 04_canonical_bytes_and_known_keys.py
"""
# Needs: pip install cryptography
import hashlib, json, time
from cryptography import exceptions
from cryptography.hazmat.primitives \
    .asymmetric import ed25519
def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True,
        separators=(",", ":")).encode()
# Demo only: the console holds this key
sk = ed25519.Ed25519PrivateKey.generate()
APPROVERS = {"k1": sk.public_key()}
REVOKED, USED = set(), set()
