"""Zero to AI Engineer · Prompting · Part 8 of 10
Slide: Defining the tool
Run: python 05_defining_the_tool.py
"""
DESC = ("Read-only. Returns status for one "
        "ticket ID the user owns.")
tools = [{
    "name": "get_ticket_status",
    "description": DESC,
    "input_schema": {"type": "object",
        "properties": {"ticket_id": {
            "type": "string",
            "pattern": "^INC[0-9]{7}$"}},
        "additionalProperties": False,
        "required": ["ticket_id"]}}]
