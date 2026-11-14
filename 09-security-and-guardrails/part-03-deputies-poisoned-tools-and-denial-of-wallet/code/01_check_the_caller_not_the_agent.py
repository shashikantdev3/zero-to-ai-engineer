"""Zero to AI Engineer · Security and Guardrails · Part 3 of 11
Slide: Check the caller, not the agent
Run: python 01_check_the_caller_not_the_agent.py
"""
TICKETS = {"t1": {"owner": "ana"}}
READERS = {"t1": {"ana"}}

def read_ticket(ticket_id, user_id):
    # service identity can read all tickets
    ticket = TICKETS[ticket_id]
    # so check the caller, not the agent
    if user_id not in READERS[ticket_id]:
        raise PermissionError("not visible")
    return ticket

print(read_ticket("t1", "ana"))
