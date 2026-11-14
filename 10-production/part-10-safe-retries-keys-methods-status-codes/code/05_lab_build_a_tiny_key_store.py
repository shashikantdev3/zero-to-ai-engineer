"""Zero to AI Engineer · Production and LLMOps · Part 10 of 38
Follow-along lab: Build a tiny key store
Run: python 05_lab_build_a_tiny_key_store.py
"""
import hashlib, json
db, made = {}, []
def handle(key, body):
    c = json.dumps(body, sort_keys=True)
    h = hashlib.sha256(c.encode()).hexdigest()
    if key not in db:
        made.append(body)
        db[key] = (h, f"ticket {len(made)}")
    old_h, result = db[key]
    return result if old_h == h else "422"
print(handle("k1", {"a": 1, "b": 2}))
print(handle("k1", {"b": 2, "a": 1}))
print(handle("k1", {"a": 9}))
print("tickets made:", len(made))
