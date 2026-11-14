"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: Wire up the graph
Run: python 10_wire_up_the_graph.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
# --- repeated from 08_state_and_a_working_node.py, 09_the_router_is_plain_python.py so this file runs on its own ---
from operator import add
from typing import Annotated, TypedDict
from langgraph.graph import (
    StateGraph, START, END)

class State(TypedDict):
    findings: Annotated[list[str], add]
    steps: int

def investigate(state):
    return {"findings": ["db latency high"],
            "steps": state["steps"] + 1}

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

# --- this slide ---
g = StateGraph(State)
g.add_node("investigate", investigate)
g.add_node("plan", plan_node)
g.add_node("escalate", escalate_node)
g.add_edge(START, "investigate")
names = ["investigate", "plan", "escalate"]
g.add_conditional_edges(
    "investigate", route,
    {n: n for n in names})
g.add_edge("plan", END)
g.add_edge("escalate", END)
app = g.compile()
