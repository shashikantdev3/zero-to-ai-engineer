"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Retry loop, part three: helpers
Run: python 05_retry_loop_part_three_helpers.py
"""
FIX = "Fix these errors. Return only JSON.\n"
def fix_request(raw, err):
    a = {"role": "assistant", "content": raw}
    note = FIX + str(err)
    u = {"role": "user", "content": note}
    return [a, u]
def check_truth(inv, text):
    probs = semantic_problems(inv)
    probs += grounding_problems(inv, text)
    if probs:
        raise NeedsHumanReview(probs)
    return inv
