"""Zero to AI Engineer · Agents and Tools · Part 20 of 26
Slide: Block when definitions change
Run: python 02_block_when_definitions_change.py
"""
# Note: run on its own, this stops with PermissionError. See the video for the context.
# --- repeated from 01_fingerprint_the_tool_definitions.py so this file runs on its own ---
import hashlib
import json

def fingerprint(tools):
    key = lambda t: t["name"]
    canon = json.dumps(sorted(tools, key=key),
                       sort_keys=True,
                       separators=(",", ":"))
    data = canon.encode()
    return hashlib.sha256(data).hexdigest()

# --- this slide ---
tools = [{"name": "send_email",
          "description": "Send an email."}]
APPROVED = {"mail": fingerprint(tools)}

# next week the server edits a description
tools[0]["description"] += " (v2)"
sid = "mail"
if fingerprint(tools) != APPROVED[sid]:
    raise PermissionError(
        f"tool definitions changed for {sid}"
        "; re-review required")
