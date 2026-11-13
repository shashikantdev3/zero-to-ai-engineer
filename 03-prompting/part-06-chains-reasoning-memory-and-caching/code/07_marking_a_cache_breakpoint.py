"""Zero to AI Engineer · Prompting · Part 6 of 10
Slide: Marking a cache breakpoint
Run: python 07_marking_a_cache_breakpoint.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
RULES = "Support rules. " * 800
stable = [{"type": "text", "text": RULES,
    "cache_control": {"type": "ephemeral"}}]
for q in ["Hi", "Refund status?"]:
    resp = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=200, system=stable,
        thinking={"type": "disabled"},
        messages=[{"role": "user",
                   "content": q}])
    print(resp.usage.cache_read_input_tokens)
