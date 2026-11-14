"""Zero to AI Engineer · Security and Guardrails · Part 9 of 11
Slide: An Allowlist Before the Prompt
Run: python 03_an_allowlist_before_the_prompt.py
"""
ALLOWED = {"ticket_id", "category",
           "description", "created_at"}
def to_prompt(ticket: dict) -> dict:
    return {k: v for k, v in ticket.items()
            if k in ALLOWED}
ticket = {
    "ticket_id": 42, "category": "billing",
    "description": "Refund please",
    "phone": "555 0100",
    "created_at": "2024-05-01",
}
print(to_prompt(ticket))
