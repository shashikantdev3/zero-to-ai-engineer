"""Zero to AI Engineer · Evaluation · Part 9 of 11
Slide: Sending Cases to Experts
Run: python 02_sending_cases_to_experts.py
"""
# --- repeated from 01_spotting_a_disagreement.py so this file runs on its own ---
BAD = {"thumbs_down", "escalated"}

def is_disagreement(t):
    judge = t["judge"]
    user = t["user_signal"]
    if judge == "PASS" and user in BAD:
        return True
    if judge == "FAIL" and user == "resolved":
        return True
    return False

# --- this slide ---
import random
def tr(j, u):
    return {"judge": j, "user_signal": u}
traces = [tr("PASS", "thumbs_down"),
          tr("FAIL", "resolved"),
          tr("PASS", "resolved")]
disagree = [t for t in traces
            if is_disagreement(t)]
k = min(100, len(disagree))
batch = random.sample(disagree, k)
print(len(batch), "cases to experts")
