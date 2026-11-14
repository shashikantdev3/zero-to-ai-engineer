"""Zero to AI Engineer · Agents and Tools · Part 16 of 26
Slide: Fallback and passthrough in a chain
Run: python 02_fallback_and_passthrough_in_a_chain.py
"""
# Needs: pip install langchain-core
# (not run while building this repo, because the package was not installed there)
# --- repeated from 01_a_failing_model_wrapped_in_retry.py so this file runs on its own ---
from langchain_core.runnables import (
    RunnableLambda, RunnableParallel,
    RunnablePassthrough)

def primary(x):
    raise TimeoutError("provider busy")

def backup(x):
    return f"backup answered: {x}"

llm = RunnableLambda(primary).with_retry(
    stop_after_attempt=2)

# --- this slide ---
llm = llm.with_fallbacks(
    [RunnableLambda(backup)])

def retriever(q):
    return "docs about " + q

chain = RunnableParallel(
    context=RunnableLambda(retriever),
    question=RunnablePassthrough())
print(chain.invoke("refunds"))
print(llm.invoke("refunds"))
