"""Zero to AI Engineer · Evaluation · Part 11 of 11
Follow-along lab: Lab: Test the Router
Run: python 06_lab_lab_test_the_router.py
"""
KNOWN_LOW = {"faq_general"}
HIGH = {"payout_request"}
def route(wf, amt):
    if wf not in KNOWN_LOW | HIGH:
        return "human_review"
    if wf in HIGH or (amt or 0) > 50_000:
        return "human_review"
    return "send_with_citations"
cases = [("faq_general", None),
         ("faq_general", 80_000),
         ("payout_v2", None),
         ("payout_request", 10)]
for wf, amt in cases:
    print(wf, "->", route(wf, amt))
