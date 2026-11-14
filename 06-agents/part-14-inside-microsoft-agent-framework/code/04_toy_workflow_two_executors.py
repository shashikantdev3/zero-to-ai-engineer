"""Zero to AI Engineer · Agents and Tools · Part 14 of 26
Slide: Toy workflow: two executors
Run: python 04_toy_workflow_two_executors.py
"""
# Toy workflow: executors and declared edges
def investigate(incident: str) -> str:
    # in real code: an agent run
    return f"evidence: {incident} cpu high"

def validate(findings: str) -> bool:
    # plain code, no model
    return findings.startswith("evidence:")

edges = {investigate: validate}
start = investigate
