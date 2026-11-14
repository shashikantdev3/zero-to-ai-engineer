"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: State and a working node
Run: python 08_state_and_a_working_node.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
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
