"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: Compile, run, read the history
Run: python 02_compile_run_read_the_history.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
# --- repeated from 01_a_tiny_graph_to_save.py so this file runs on its own ---
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

# --- this slide ---
# production: a Postgres checkpointer
app = g.compile(checkpointer=InMemorySaver())
cfg = {"configurable":
       {"thread_id": "incident-4711"}}
app.invoke({"steps": 0}, cfg)
for snap in app.get_state_history(cfg):
    print(snap.values.get("steps"), snap.next)
