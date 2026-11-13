"""Zero to AI Engineer · Prompting · Part 7 of 10
Slide: The Template Text
Run: python 01_the_template_text.py
"""
# Needs: pip install langchain_core
# (not run while building this repo, because the package was not installed there)
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
