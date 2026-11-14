"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 8 of 10
Slide: Prompt caching with a cache marker
Run: python 03_prompt_caching_with_a_cache_marker.py
"""
# Needs: pip install anthropic
# Note: this calls a model, so it needs your key in ANTHROPIC_API_KEY (see SETUP.md).
# (not run while building this repo)
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
BIG_TEXT = "You are a support agent. " * 400
block = {"type": "text", "text": BIG_TEXT}
block["cache_control"] = {"type": "ephemeral"}
msgs = [{"role": "user", "content": "Hi"}]
resp = client.messages.create(
    model=MODEL, max_tokens=200,
    thinking={"type": "disabled"},
    system=[block], messages=msgs)
print(resp.usage.cache_read_input_tokens)
