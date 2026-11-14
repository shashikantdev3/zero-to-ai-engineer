"""Zero to AI Engineer · Agents and Tools · Part 23 of 26
Slide: Scoring a trajectory
Run: python 05_scoring_a_trajectory.py
"""
def subseq_score(exp, act):
    # share of expected calls seen in order
    i = 0
    for tool in act:
        if i < len(exp) and tool == exp[i]:
            i += 1
    return i / len(exp) if exp else 1.0
