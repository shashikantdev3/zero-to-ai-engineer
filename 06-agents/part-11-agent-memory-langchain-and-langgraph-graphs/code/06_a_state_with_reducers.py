"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: A state with reducers
Run: python 06_a_state_with_reducers.py
"""
# Needs: pip install langgraph
# (not run while building this repo, because the package was not installed there)
from typing import Annotated, TypedDict
from operator import add
from langgraph.graph.message import (
    add_messages)
class State(TypedDict):
    # merges by message ID, appends new
    messages: Annotated[list, add_messages]
    # parallel nodes can both append
    findings: Annotated[list[str], add]
    # steps and approved: plain overwrite
    steps: int
    approved: bool
