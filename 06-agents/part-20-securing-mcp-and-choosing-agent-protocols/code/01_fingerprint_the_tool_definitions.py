"""Zero to AI Engineer · Agents and Tools · Part 20 of 26
Slide: Fingerprint the tool definitions
Run: python 01_fingerprint_the_tool_definitions.py
"""
import hashlib
import json

def fingerprint(tools):
    key = lambda t: t["name"]
    canon = json.dumps(sorted(tools, key=key),
                       sort_keys=True,
                       separators=(",", ":"))
    data = canon.encode()
    return hashlib.sha256(data).hexdigest()
