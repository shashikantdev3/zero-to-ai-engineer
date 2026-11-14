"""Zero to AI Engineer · Production and LLMOps · Part 2 of 38
Slide: Build a batch file
Run: python 03_build_a_batch_file.py
"""
import json

tickets = {1042: "Printer jams daily.",
           1043: "Login fails on mobile."}
for tid, text in tickets.items():
    msg = {"role": "user",
           "content": "Summarise: " + text}
    req = {"custom_id": f"ticket-{tid}",
           "body": {"messages": [msg]}}
    # one JSON line per request
    print(json.dumps(req))
