"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Follow-along lab: Spot the repeating fingerprint
Run: python 09_lab_spot_the_repeating_fingerprint.py
"""
import hashlib, json
def fp(node, state):
    raw = json.dumps(state, sort_keys=True)
    h = hashlib.sha256(raw.encode())
    return node, h.hexdigest()[:8]
seen = set()
trail = [("a", {"x": 1}), ("a", {"x": 2}),
         ("b", {"x": 2}), ("a", {"x": 1})]
for node, state in trail:
    f = fp(node, state)
    tag = "SEEN" if f in seen else "new"
    print(node, state, f[1], tag)
    seen.add(f)
print("unique steps:", len(seen))
