"""Zero to AI Engineer · Evaluation · Part 9 of 11
Slide: Spotting a Disagreement
Run: python 01_spotting_a_disagreement.py
"""
BAD = {"thumbs_down", "escalated"}

def is_disagreement(t):
    judge = t["judge"]
    user = t["user_signal"]
    if judge == "PASS" and user in BAD:
        return True
    if judge == "FAIL" and user == "resolved":
        return True
    return False
