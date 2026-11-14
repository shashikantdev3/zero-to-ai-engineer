"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: A tiny graph to save
Run: python 01_a_tiny_graph_to_save.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
from typing import TypedDict
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import (
    InMemorySaver)
class S(TypedDict):
    steps: int
def work(state: S):
    return {"steps": state["steps"] + 1}
g = StateGraph(S)
g.add_node("work", work)
g.set_entry_point("work")
g.set_finish_point("work")
