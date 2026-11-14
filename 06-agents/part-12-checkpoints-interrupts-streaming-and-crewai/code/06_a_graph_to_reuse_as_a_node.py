"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: A graph to reuse as a node
Run: python 06_a_graph_to_reuse_as_a_node.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
from typing import TypedDict
from langgraph.graph import StateGraph
class S(TypedDict):
    steps: int
def work(state: S):
    return {"steps": state["steps"] + 1}
g = StateGraph(S)
g.add_node("work", work)
g.set_entry_point("work")
g.set_finish_point("work")
app = g.compile()
