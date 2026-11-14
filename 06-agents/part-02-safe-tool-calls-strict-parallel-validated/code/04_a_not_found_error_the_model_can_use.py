"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: A not-found error the model can use
Run: python 04_a_not_found_error_the_model_can_use.py
"""
import json

call_id = "tu_1"
hint = ("No order ORD-123456 for this user. "
        "Ask the user to confirm the ID.")
result = {
    "type": "tool_result",
    "tool_use_id": call_id,
    "is_error": True,
    "content": json.dumps({"ok": False,
        "error": "NOT_FOUND", "hint": hint}),
}
