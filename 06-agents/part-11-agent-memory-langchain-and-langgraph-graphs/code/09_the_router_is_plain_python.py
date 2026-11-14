"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: The router is plain Python
Run: python 09_the_router_is_plain_python.py
"""
def route(state):
    if state["steps"] >= 5:
        return "escalate"
    if state["findings"]:
        return "plan"
    return "investigate"

def plan_node(state):
    return {}

def escalate_node(state):
    return {}
