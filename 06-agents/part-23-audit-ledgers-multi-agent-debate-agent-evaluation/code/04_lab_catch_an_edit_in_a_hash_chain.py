"""Zero to AI Engineer · Agents and Tools · Part 23 of 26
Follow-along lab: Catch an edit in a hash chain
Run: python 04_lab_catch_an_edit_in_a_hash_chain.py
"""
import hashlib
def build(recs, prev="0" * 64):
    out = []
    for r in recs:
        s = (prev + "|" + r).encode()
        prev = hashlib.sha256(s).hexdigest()
        out.append(prev)
    return out
recs = ["pay 5", "deny 7", "pay 9"]
stored = build(recs)
recs[1] = "pay 7"
fresh = build(recs)
for i, a, b in zip(range(3), stored, fresh):
    print("entry", i, "intact:", a == b)
