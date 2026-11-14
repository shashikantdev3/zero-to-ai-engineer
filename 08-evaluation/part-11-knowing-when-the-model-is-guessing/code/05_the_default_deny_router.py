"""Zero to AI Engineer · Evaluation · Part 11 of 11
Slide: The Default-Deny Router
Run: python 05_the_default_deny_router.py
"""
def route(wf, tool, amt, hint=None):
    # default deny: unknown goes to a human
    if wf is None or wf not in KNOWN:
        return "human_review"
    tier = 1 if wf in MEDIUM else 0
    if wf in HIGH or tool in HIGH_TOOLS:
        tier = 2
    if amt is not None and amt > 50_000:
        tier = 2
    if hint in TIERS:
        tier = max(tier, TIERS.index(hint))
    return TIERS[tier]
