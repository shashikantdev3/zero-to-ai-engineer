"""Zero to AI Engineer · RAG and Vector Search · Part 17 of 26
Slide: One small model call
Run: python 02_one_small_model_call.py
"""
# Needs: pip install anthropic
# --- repeated from 01_building_the_rewrite_prompt.py so this file runs on its own ---
history = (
    "User: What's the parental leave rule?\n"
    "Assistant: Here is the staff policy.")
message = "and what about for contractors?"
rewrite_prompt = (
    "Rewrite the last user message as a "
    "standalone search query. Use the "
    "conversation only to resolve "
    "references. Return only the query.\n\n"
    f"{history}\nUser: {message}"
)

# --- this slide ---
import anthropic
client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=100,
    thinking={"type": "disabled"},
    messages=[{"role": "user",
               "content": rewrite_prompt}],
)
standalone = resp.content[0].text
print("original:", message)
print("rewrite:", standalone)
