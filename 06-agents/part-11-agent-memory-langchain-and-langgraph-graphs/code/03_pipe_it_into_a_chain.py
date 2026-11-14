"""Zero to AI Engineer · Agents and Tools · Part 11 of 26
Slide: Pipe it into a chain
Run: python 03_pipe_it_into_a_chain.py
"""
# Needs: pip install langchain_anthropic langchain-core
# (not run while building this repo, because the package was not installed there)
# --- repeated from 02_a_prompt_template.py so this file runs on its own ---
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

# --- this slide ---
model = ChatAnthropic(
    model="claude-haiku-5-5", max_tokens=200,
    thinking={"type": "disabled"})
chain = prompt | model | StrOutputParser()
print(chain.invoke({"logs": "db timeouts"}))
