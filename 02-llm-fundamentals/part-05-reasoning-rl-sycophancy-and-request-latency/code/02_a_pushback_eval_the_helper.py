"""Zero to AI Engineer · LLM Fundamentals · Part 5 of 18
Slide: A Pushback Eval: The Helper
Run: python 02_a_pushback_eval_the_helper.py
"""
# Needs: pip install anthropic
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"

def ask(msgs):
    resp = client.messages.create(
        model=MODEL, max_tokens=200,
        thinking={"type": "disabled"},
        messages=msgs,
    )
    return resp.content[0].text
