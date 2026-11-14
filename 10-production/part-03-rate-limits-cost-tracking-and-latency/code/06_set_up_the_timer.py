"""Zero to AI Engineer · Production and LLMOps · Part 3 of 38
Slide: Set up the timer
Run: python 06_set_up_the_timer.py
"""
# Needs: pip install anthropic
import time
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
msgs = [{"role": "user",
         "content": "Explain DNS briefly."}]
t0 = time.perf_counter()
first, n = None, 0
