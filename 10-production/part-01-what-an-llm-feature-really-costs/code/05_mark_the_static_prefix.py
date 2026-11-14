"""Zero to AI Engineer · Production and LLMOps · Part 1 of 38
Slide: Mark the static prefix
Run: python 05_mark_the_static_prefix.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
# static part first, identical every call
GUIDE = "You answer billing questions. " * 500
cc = {"type": "ephemeral"}
system = [{"type": "text", "text": GUIDE,
           "cache_control": cc}]
