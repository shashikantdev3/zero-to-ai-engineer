"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 23 of 28
Follow-along lab: Hash users into variants
Run: python 01_lab_hash_users_into_variants.py
"""
import hashlib

def variant(user_id: str) -> str:
    h = hashlib.sha256(user_id.encode())
    n = int(h.hexdigest(), 16) % 100
    return "A" if n < 50 else "B"

for uid in ["u1", "u2", "u3"]:
    print(uid, variant(uid))
print("again:", variant("u1"))
users = [f"u{i}" for i in range(10000)]
share = sum(variant(u) == "A" for u in users)
print("A share:", share / 10000)
