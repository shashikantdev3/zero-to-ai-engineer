"""Zero to AI Engineer · Prompting · Part 8 of 10
Slide: Validate, check, then run
Run: python 07_validate_check_then_run.py
"""
def run_tool(block, user) -> dict:
    try:
        args = TicketArgs.model_validate(
            block.input)
    except ValidationError:
        return {"error": "invalid arguments"}
    tid = args.ticket_id
    if not TICKET_ID.fullmatch(tid):
        return {"error": "invalid ticket_id"}
    if not user_owns_ticket(user, tid):
        return {"error": "not permitted"}
    return ticket_status(tid)
