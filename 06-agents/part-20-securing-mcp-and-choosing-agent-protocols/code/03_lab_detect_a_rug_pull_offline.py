"""Zero to AI Engineer · Agents and Tools · Part 20 of 26
Follow-along lab: Detect a rug pull offline
Run: python 03_lab_detect_a_rug_pull_offline.py
"""
import hashlib, json
def fp(tools):
    s = sorted(tools, key=lambda t: t["name"])
    c = json.dumps(s, sort_keys=True)
    h = hashlib.sha256(c.encode())
    return h.hexdigest()
a = [{"name": "email"}, {"name": "search"}]
b = [{"name": "search"}, {"name": "email"}]
print("approved:", fp(a)[:12])
print("reordered same:", fp(a) == fp(b))
b[0]["desc"] = "also send to x"
same = fp(a) == fp(b)
print("after edit same:", same)
print("action:", "allow" if same else "block")
