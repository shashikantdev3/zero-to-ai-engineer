"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: The tool, in a stable order
Run: python 07_the_tool_in_a_stable_order.py
"""
# --- repeated from 06_the_argument_schema.py so this file runs on its own ---
args_schema = {
    "type": "object",
    "properties": {
        "service": {"type": "string",
            "enum": ["api", "worker",
                     "scheduler"]},
        "reason": {"type": "string",
                   "maxLength": 300},
    },
    "required": ["service", "reason"],
    "additionalProperties": False,
}

# --- this slide ---
restart_tool = {
    "name": "request_restart",
    "description": (
        "Request a restart of ONE service. "
        "Does not restart anything. Creates "
        "a change request that a human "
        "must approve."),
    "input_schema": args_schema,
}
# same order on every request
tools = sorted([restart_tool],
               key=lambda t: t["name"])
