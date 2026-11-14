"""Zero to AI Engineer · Agents and Tools · Part 21 of 26
Follow-along lab: Break the evidence check
Run: python 03_lab_break_the_evidence_check.py
"""
ev = {"log1": "ERROR  disk full on db-2"}
def check(src, quote):
    if src not in ev:
        return "unknown source"
    q = " ".join(quote.split())
    if len(q) < 12:
        return "too short"
    text = " ".join(ev[src].split())
    return "ok" if q in text else "no match"
print("naive check:", "" in ev["log1"])
print(check("log1", "ERROR disk full"))
print(check("log1", "   "))
print(check("log9", "ERROR disk full"))
print(check("log1", "disk full on db-3"))
