"""Zero to AI Engineer · RAG and Vector Search · Part 19 of 26
Slide: One Text for Both Indexes
Run: python 06_one_text_for_both_indexes.py
"""
# Needs: pip install anthropic
# --- repeated from 05_preparing_the_context_prompt.py so this file runs on its own ---
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

# --- this slide ---
resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=100,
    thinking={"type": "disabled"},
    system=system,
    messages=[{"role": "user",
               "content": ask}],
)
ctx = resp.content[0].text
# one text for BOTH embedding and BM25
indexed_text = f"{ctx}\n{chunk}"
print(indexed_text)
