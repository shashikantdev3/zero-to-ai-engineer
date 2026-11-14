"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: A toy judge: quote matching
Run: python 05_a_toy_judge_quote_matching.py
"""
# --- repeated from 03_the_groundedness_judge_prompt.py, 04_scoring_the_share_of_supported_claims.py so this file runs on its own ---
JUDGE = """Context:
{context}

Claim: {claim}

Is the claim fully supported by the context?
Answer only SUPPORTED or NOT_SUPPORTED."""

def groundedness(claims, context, judge):
    verdicts = [
        judge(JUDGE.format(
            context=context, claim=c)).strip()
        for c in claims
    ]
    hits = [v == "SUPPORTED" for v in verdicts]
    return sum(hits) / max(len(claims), 1)

# --- this slide ---
def quote(prompt):
    ctx, rest = prompt.split("Claim: ")
    claim = rest.split("\n")[0]
    if claim in ctx:
        return "SUPPORTED"
    return "NOT_SUPPORTED"

context = "Staff get 20 leave days a year."
claims = ["Staff get 20 leave days a year",
          "Unused days expire in March"]
print(groundedness(claims, context, quote))
