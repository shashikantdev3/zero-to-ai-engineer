"""Zero to AI Engineer · LLM Fundamentals · Part 14 of 18
Slide: Penalties, Simulated Offline
Run: python 06_penalties_simulated_offline.py
"""
# made-up logits for the next token
logits = {"good": 2.0, "new": 1.5,
          "fun": 1.0}
counts = {"good": 3, "new": 0, "fun": 1}
presence, frequency = 0.4, 0.3
for tok, c in counts.items():
    if c > 0:
        logits[tok] -= presence
    logits[tok] -= frequency * c
print(logits)
# marketing copy: penalties like these
# JSON extractor: leave both at 0
