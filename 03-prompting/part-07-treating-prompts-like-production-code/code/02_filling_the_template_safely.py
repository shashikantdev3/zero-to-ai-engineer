"""Zero to AI Engineer · Prompting · Part 7 of 10
Slide: Filling the Template Safely
Run: python 02_filling_the_template_safely.py
"""
# Note: run on its own, this stops with ModuleNotFoundError. See the video for the context.
# --- repeated from 01_the_template_text.py so this file runs on its own ---
from langchain_core import prompts

# literal braces doubled
SYS_V3 = (
    'Return JSON like '
    '{{"category": "network"}}.'
)
USER = (
    "<documents>{docs}</documents>\n"
    "<question>{question}</question>"
)

# --- this slide ---
# content arrives as values
docs = 'Page text: {"a": 1}'
q = "Why is the VPN down?"
CPT = prompts.ChatPromptTemplate
prompt = CPT.from_messages(
    [("system", SYS_V3), ("user", USER)]
)
# passed as values, not concatenated
msgs = prompt.invoke(
    {"docs": docs, "question": q}
)
