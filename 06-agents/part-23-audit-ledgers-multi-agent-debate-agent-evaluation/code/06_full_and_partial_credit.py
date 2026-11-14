"""Zero to AI Engineer · Agents and Tools · Part 23 of 26
Slide: Full and partial credit
Run: python 06_full_and_partial_credit.py
"""
# --- repeated from 05_scoring_a_trajectory.py so this file runs on its own ---
def subseq_score(exp, act):
    # share of expected calls seen in order
    i = 0
    for tool in act:
        if i < len(exp) and tool == exp[i]:
            i += 1
    return i / len(exp) if exp else 1.0

# --- this slide ---
expected = ["get_status", "get_logs",
            "request_change"]
actual = ["get_status", "get_deploys",
          "get_logs", "request_change"]
assert subseq_score(expected, actual) == 1.0
# skipped the logs step: partial credit
short = ["get_status", "request_change"]
print(round(subseq_score(expected, short), 2))
