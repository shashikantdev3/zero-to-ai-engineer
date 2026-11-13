"""Zero to AI Engineer · Python · Part 19 of 25
Slide: Type-only imports
Run: python 08_type_only_imports.py
"""
# Needs: pip install myapp
# retriever.py
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # not imported at runtime, so no cycle
    from myapp.agent import Agent

def search(agent: Agent, q: str) -> list[str]:
    return []
# CLIENT = make_client()
# runs on first import only; avoid network
