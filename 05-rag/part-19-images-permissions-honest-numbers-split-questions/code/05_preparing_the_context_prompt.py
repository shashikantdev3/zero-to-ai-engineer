"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: Preparing the Context Prompt
Run: python 05_preparing_the_context_prompt.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
doc = "Leave policy. Section 4: carry-over."
chunk = "Up to five days carry over."
system = [{
    "type": "text",
    "text": f"<document>{doc}</document>",
    "cache_control": {"type": "ephemeral"},
}]
ask = f"<chunk>{chunk}</chunk>\n" + (
    "Place this chunk in the document in "
    "one short sentence. Return only that.")
