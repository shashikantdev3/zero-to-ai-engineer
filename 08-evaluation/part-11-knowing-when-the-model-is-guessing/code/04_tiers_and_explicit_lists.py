"""Zero to AI Engineer · Evaluation · Part 11 of 11
Slide: Tiers and Explicit Lists
Run: python 04_tiers_and_explicit_lists.py
"""
TIERS = ["send_with_citations",
         "verify_then_send", "human_review"]
# explicit allowlist for the lowest tier
LOW = {"faq_general", "office_locations"}
MEDIUM = {"policy_explanation"}
HIGH = {"claims_portal", "payout_request"}
HIGH_TOOLS = {"issue_payout", "deny_claim"}
KNOWN = LOW | MEDIUM | HIGH
