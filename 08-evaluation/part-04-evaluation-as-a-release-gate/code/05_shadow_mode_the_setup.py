"""Zero to AI Engineer · Evaluation · Part 4 of 11
Slide: Shadow mode: the setup
Run: python 05_shadow_mode_the_setup.py
"""
import asyncio
_tasks: set[asyncio.Task] = set()

async def current(req):
    return "old answer"

async def candidate(req):
    # proposes actions, never executes
    return "new answer"

def log_shadow(req, result, error):
    print("shadow log:", result, error)
