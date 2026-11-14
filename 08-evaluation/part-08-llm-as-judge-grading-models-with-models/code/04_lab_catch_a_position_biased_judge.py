"""Zero to AI Engineer · Evaluation · Part 8 of 11
Follow-along lab: Catch a position-biased judge
Run: python 04_lab_catch_a_position_biased_judge.py
"""
# a and b are the true quality of answers
def judge(a, b):
    # position bias: slot A wins close calls
    return "B" if b - a > 2 else "A"
def both(a, b):
    v1, v2 = judge(a, b), judge(b, a)
    if (v1, v2) == ("A", "B"):
        return "A"
    if (v1, v2) == ("B", "A"):
        return "B"
    return "TIE"
for a, b in [(5, 6), (6, 5), (2, 9)]:
    print(a, "vs", b, "single:", judge(a, b),
          "both:", both(a, b))
