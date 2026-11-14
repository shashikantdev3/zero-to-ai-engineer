"""Zero to AI Engineer · Security and Guardrails · Part 7 of 11
Slide: Guard stand-ins
Run: python 02_guard_stand_ins.py
"""
def refuse(w="blocked"): return "No: " + w
def redact_pii(t):
    return t.replace("555-0100", "[PHONE]")
def injection_detected(t):
    return "ignore previous" in t.lower()
def log_block(kind): print("blocked:", kind)
def llm(t, user): return f"Answer for {user}"
def safe(r): return "hate" not in r
def leaks_pii(r): return "555-0100" in r
def grounded(r): return True
def fallback(): return "Sorry, I cannot answer."
MAX_CHARS = 2000
