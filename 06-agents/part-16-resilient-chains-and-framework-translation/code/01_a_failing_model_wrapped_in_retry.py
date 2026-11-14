"""Zero to AI Engineer · Agents and Tools · Part 16 of 26
Slide: A failing model, wrapped in retry
Run: python 01_a_failing_model_wrapped_in_retry.py
"""
# Needs: pip install langchain-core
# (not run while building this repo, because the package was not installed there)
from langchain_core.runnables import (
    RunnableLambda, RunnableParallel,
    RunnablePassthrough)

def primary(x):
    raise TimeoutError("provider busy")

def backup(x):
    return f"backup answered: {x}"

llm = RunnableLambda(primary).with_retry(
    stop_after_attempt=2)
