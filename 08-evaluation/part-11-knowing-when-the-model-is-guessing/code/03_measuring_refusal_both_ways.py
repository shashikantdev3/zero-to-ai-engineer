"""Zero to AI Engineer · Evaluation · Part 11 of 11
Slide: Measuring Refusal Both Ways
Run: python 03_measuring_refusal_both_ways.py
"""
def rate(rows):
    hits = sum(r["abstained"] for r in rows)
    return hits / max(len(rows), 1)
def abstention_metrics(results):
    should = [r for r in results
              if r["must_abstain"]]
    shouldnt = [r for r in results
                if not r["must_abstain"]]
    return {
        "correct_refusal_rate": rate(should),
        "over_refusal_rate": rate(shouldnt),
    }
