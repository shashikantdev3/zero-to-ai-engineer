"""Zero to AI Engineer · Python · Part 8 of 25
Slide: The agent holds its parts
Run: python 09_the_agent_holds_its_parts.py
"""
from __future__ import annotations
# composition: the agent has its parts
class Agent:
    def __init__(self, llm: LLMClient,
                 retriever: Retriever):
        self.llm = llm
        self.retriever = retriever
    def answer(self, q: str) -> str:
        hits = self.retriever.search(q, k=3)
        ctx = "\n".join(hits)
        prompt = f"{ctx}\n\nQ: {q}"
        return self.llm.complete(prompt)
