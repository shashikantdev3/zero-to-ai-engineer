"""Zero to AI Engineer · Agents and Tools · Part 3 of 26
Slide: Allowed tools and real records
Run: python 03_allowed_tools_and_real_records.py
"""
from types import SimpleNamespace as NS
POLICY_MAX_INR = 50_000
ALLOWED = {
    "track_order":
        {"get_order", "get_shipment"},
    "refund_request":
        {"get_order", "propose_refund"},
}
orders = {"A1": NS(owner="u1",
                   refundable_inr=48_000)}
