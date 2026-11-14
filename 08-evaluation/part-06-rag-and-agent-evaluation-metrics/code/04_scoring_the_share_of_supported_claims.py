"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: Scoring the share of supported claims
Run: python 04_scoring_the_share_of_supported_claims.py
"""
def groundedness(claims, context, judge):
    verdicts = [
        judge(JUDGE.format(
            context=context, claim=c)).strip()
        for c in claims
    ]
    hits = [v == "SUPPORTED" for v in verdicts]
    return sum(hits) / max(len(claims), 1)
