"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: A prompt template
Run: python 02_a_prompt_template.py
"""
# Needs: pip install langchain_anthropic langchain-core
# (not run while building this repo, because the package was not installed there)
from langchain_core.prompts import (
    ChatPromptTemplate)
from langchain_core.output_parsers import (
    StrOutputParser)
from langchain_anthropic import ChatAnthropic

prompt = ChatPromptTemplate.from_messages([
    ("system", "Summarise the incident "
               "in two sentences."),
    ("human", "{logs}"),
])
