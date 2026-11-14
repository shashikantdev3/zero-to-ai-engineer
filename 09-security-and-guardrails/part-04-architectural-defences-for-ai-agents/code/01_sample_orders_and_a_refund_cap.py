"""Zero to AI Engineer · Security and Guardrails · Part 4 of 11
Slide: Sample orders and a refund cap
Run: python 01_sample_orders_and_a_refund_cap.py
"""
from dataclasses import dataclass

SELF_MAX = 5000

@dataclass
class Order:
    owner: str
    refundable: int
    eligible: bool = True

orders = {"A1": Order("u1", 3000)}
