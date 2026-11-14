"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: A node that asks a human
Run: python 04_a_node_that_asks_a_human.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
from typing import TypedDict
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import (
    InMemorySaver)
class S(TypedDict):
    plan: str
    approved: bool
def approval(state: S):
    # anything up here runs twice on resume
    decision = interrupt(
        {"plan": state["plan"]})
    return {"approved": decision == "yes"}
