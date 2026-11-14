"""Zero to AI Engineer · RAG and Vector Search · Part 23 of 26
Slide: The context recall function
Run: python 04_the_context_recall_function.py
"""
# --- repeated from 03_a_toy_judge.py so this file runs on its own ---
class ToyJudge:
    def split_claims(self, text):
        parts = text.split(".")
        return [p.strip() for p in parts
                if p.strip()]

    def is_supported(self, claim, texts):
        low = claim.lower()
        return any(low in t.lower()
                   for t in texts)

# --- this slide ---
def context_recall(ref, texts, judge):
    claims = judge.split_claims(ref)
    supported = sum(judge.is_supported(c, texts)
                    for c in claims)
    if not claims:
        return 1.0
    return supported / len(claims)

ref = "Refunds take 5 days. Fees are waived"
chunks = ["refunds take 5 days on orders"]
print(context_recall(ref, chunks, ToyJudge()))
