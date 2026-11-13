"""Zero to AI Engineer · Prompting · Part 6 of 10
Slide: Extract, check, then draft
Run: python 02_extract_check_then_draft.py
"""
# --- repeated from 01_one_helper_for_every_call.py so this file runs on its own ---
import json
import anthropic
client = anthropic.Anthropic()
SMALL = "claude-haiku-5-5"
BIG = "claude-sonnet-5-5"
def llm(model, system, text):
    r = client.messages.create(
        model=model, max_tokens=1000,
        system=system,
        messages=[{"role": "user",
                   "content": text}])
    # skip any thinking block
    return "".join(b.text for b in r.content
                   if b.type == "text")

# --- this slide ---
ticket = "Order 1234 arrived broken."
raw = llm(SMALL,
          "Reply with raw JSON only: "
          "keys order_id and issue.",
          ticket)
facts = json.loads(raw)
# code gate: stop a bad extraction early
if not facts.get("order_id"):
    raise ValueError("extraction failed")
# step 2: bigger model drafts the reply
reply = llm(BIG, "Draft a polite reply.",
            json.dumps(facts))
print(reply)
