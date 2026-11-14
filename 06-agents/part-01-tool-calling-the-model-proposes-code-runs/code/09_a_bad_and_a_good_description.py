"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: A bad and a good description
Run: python 09_a_bad_and_a_good_description.py
"""
bad = {"name": "get_ticket",
       "description": "Ticket API"}
good = {"name": "get_ticket",
    "description": (
        "Read-only. Returns status, owner "
        "and last update for ONE existing "
        "ticket. Use when the user gives a "
        "ticket number. Do not use to "
        "create tickets; use create_ticket "
        "for that.")}
