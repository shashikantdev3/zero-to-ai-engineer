"""Zero to AI Engineer · Security and Guardrails · Part 2 of 11
Slide: A tripwire, not a wall
Run: python 01_a_tripwire_not_a_wall.py
"""
# Cheap tripwire: log and score only.
SUSPICIOUS = ("ignore previous",
              "disregard the above",
              "system prompt")

def tripwire(text: str) -> bool:
    t = text.lower()
    return any(p in t for p in SUSPICIOUS)

print(tripwire("IGNORE previous rules"))
print(tripwire("Disregard everything above"))
