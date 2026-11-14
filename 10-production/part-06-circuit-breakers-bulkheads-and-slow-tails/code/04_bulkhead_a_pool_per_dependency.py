"""Zero to AI Engineer · Production and LLMOps · Part 6 of 38
Slide: Bulkhead: a pool per dependency
Run: python 04_bulkhead_a_pool_per_dependency.py
"""
import asyncio

pools = {"llm": asyncio.Semaphore(50),
         "search": asyncio.Semaphore(100),
         "parser": asyncio.Semaphore(5)}
async def slow_parse(doc):
    await asyncio.sleep(0.1)
    return doc.upper()
async def parse_document(doc):
    # at most 5 parses; chat is unaffected
    async with pools["parser"]:
        return await slow_parse(doc)
