"""Zero to AI Engineer · Security and Guardrails · Part 11 of 11
Follow-along lab: Audit an Agent Inventory
Run: python 03_lab_audit_an_agent_inventory.py
"""
agents = [
    ("support-bot", "ops-team", "2025-01-10"),
    ("refund-bot", None, "2024-11-02"),
    ("search-bot", "data-team", "2023-06-30"),
]
TODAY = "2024-12-01"
for name, owner, expiry in agents:
    if owner is None:
        print(f"{name}: orphan, disable")
    elif expiry < TODAY:
        print(f"{name}: expired, review")
    else:
        print(f"{name}: ok, owner {owner}")
print(f"agents checked: {len(agents)}")
