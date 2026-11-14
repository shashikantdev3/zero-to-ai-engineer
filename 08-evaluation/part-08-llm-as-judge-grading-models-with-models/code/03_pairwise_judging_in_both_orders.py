"""Zero to AI Engineer · Evaluation · Part 8 of 11
Slide: Pairwise judging in both orders
Run: python 03_pairwise_judging_in_both_orders.py
"""
PAIRWISE = ("Q: {q}\nA: {a}\nB: {b}\n"
            "Ignore length. A, B or TIE?")
def debiased(q, a, b, judge):
    p1 = PAIRWISE.format(q=q, a=a, b=b)
    p2 = PAIRWISE.format(q=q, a=b, b=a)
    v1 = judge(p1).strip().splitlines()[-1]
    v2 = judge(p2).strip().splitlines()[-1]
    if v1 == "A" and v2 == "B":
        return "A"
    if v1 == "B" and v2 == "A":
        return "B"
    return "TIE"
