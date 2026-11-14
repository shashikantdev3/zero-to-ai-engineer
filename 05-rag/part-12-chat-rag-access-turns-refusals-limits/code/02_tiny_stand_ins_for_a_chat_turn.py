"""Zero to AI Engineer · RAG and Vector Search · Part 12 of 26
Slide: Tiny stand-ins for a chat turn
Run: python 02_tiny_stand_ins_for_a_chat_turn.py
"""
from types import SimpleNamespace as NS
def rewrite_standalone(summ, recent, msg):
    return f"{summ} {msg}".strip()
def retrieve(query, user):
    return [f"chunk for: {query}"]
def generate(summ, recent, chunks, msg):
    return f"answer using {len(chunks)} chunk"
def summarise(summ, old):
    return f"{summ} +{len(old)} turns".strip()
state = NS(summ="", recent=[])
