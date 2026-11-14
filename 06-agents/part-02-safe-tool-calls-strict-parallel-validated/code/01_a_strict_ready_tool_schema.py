"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: A strict-ready tool schema
Run: python 01_a_strict_ready_tool_schema.py
"""
props = {
    "order_id": {"type": "string"},
    "note": {"type": ["string", "null"]},
}
get_order = {"name": "get_order",
    "input_schema": {
        "type": "object",
        "properties": props,
        "required": ["order_id", "note"],
        "additionalProperties": False,
    },
}
