"""Zero to AI Engineer · LLM Fundamentals · Part 17 of 18
Slide: Pin the Model, Log the Version
Run: python 04_pin_the_model_log_the_version.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
# exact model ID, not a moving alias
MODEL = "claude-haiku-5-5"
PROMPT_V = "triage-v3"
resp = client.messages.create(
    model=MODEL, max_tokens=200,
    thinking={"type": "disabled"},
    messages=[{"role": "user",
               "content": "Say hi"}])
# record what actually served the call
print({"model": resp.model,
       "prompt_version": PROMPT_V})
