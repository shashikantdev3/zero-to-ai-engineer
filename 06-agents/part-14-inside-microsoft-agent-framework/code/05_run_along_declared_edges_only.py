"""Zero to AI Engineer · Agents and Tools · Part 14 of 26
Slide: Run along declared edges only
Run: python 05_run_along_declared_edges_only.py
"""
# --- repeated from 04_toy_workflow_two_executors.py so this file runs on its own ---
# Toy workflow: executors and declared edges
def investigate(incident: str) -> str:
    # in real code: an agent run
    return f"evidence: {incident} cpu high"

def validate(findings: str) -> bool:
    # plain code, no model
    return findings.startswith("evidence:")

edges = {investigate: validate}
start = investigate

# --- this slide ---
def run(start, message):
    node = start
    # next node comes only from declared edges
    while node is not None:
        message = node(message)
        node = edges.get(node)
    return message

print(run(start, "api slow"))
