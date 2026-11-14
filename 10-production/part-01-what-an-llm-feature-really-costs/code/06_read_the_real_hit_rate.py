"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: Read the real hit rate
Run: python 06_read_the_real_hit_rate.py
"""
# Needs: pip install anthropic
# Note: this calls a model, so it needs your key in ANTHROPIC_API_KEY (see SETUP.md).
# (not run while building this repo)
# --- repeated from 05_mark_the_static_prefix.py so this file runs on its own ---
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
# static part first, identical every call
GUIDE = "You answer billing questions. " * 500
cc = {"type": "ephemeral"}
system = [{"type": "text", "text": GUIDE,
           "cache_control": cc}]

# --- this slide ---
# variable part last: the user turn
for q in ["Refund status?", "Invoice copy?"]:
    resp = client.messages.create(
        model=MODEL, max_tokens=200,
        thinking={"type": "disabled"},
        system=system,
        messages=[{"role": "user",
                   "content": q}])
    print(resp.usage.cache_read_input_tokens)
    print(resp.content[0].text)
