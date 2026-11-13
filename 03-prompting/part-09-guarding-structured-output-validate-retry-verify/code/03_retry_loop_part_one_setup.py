"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Retry loop, part one: setup
Run: python 03_retry_loop_part_one_setup.py
"""
# Needs: pip install anthropic pydantic
import anthropic
from pydantic import ValidationError
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"

class NeedsHumanReview(Exception):
    pass
def llm(msgs):
    resp = client.messages.create(
        model=MODEL, max_tokens=300,
        thinking={"type": "disabled"},
        system=EXTRACT_V2, messages=msgs)
    return resp.content[0].text
