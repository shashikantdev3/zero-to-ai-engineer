"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: Plug it in, stream updates
Run: python 07_plug_it_in_stream_updates.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
# --- repeated from 06_a_graph_to_reuse_as_a_node.py so this file runs on its own ---
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

# --- this slide ---
parent = StateGraph(S)
# a compiled graph used as one node
parent.add_node("investigate", app)
parent.set_entry_point("investigate")
parent.set_finish_point("investigate")
top = parent.compile()
# one entry per step: {node: changes}
for chunk in top.stream(
        {"steps": 0}, stream_mode="updates"):
    print(chunk)
