"""Zero to AI Engineer · Python · Part 2 of 25
Slide: match on Tool-Call Payloads
Run: python 04_match_on_tool_call_payloads.py
"""
def handle(event: dict) -> str:
    match event:
        case {"type": "tool_call",
              "name": str(name)}:
            return f"call {name}"
        case {"type": "text",
              "content": str(text)}:
            return text
        case _:
            return "unknown"
