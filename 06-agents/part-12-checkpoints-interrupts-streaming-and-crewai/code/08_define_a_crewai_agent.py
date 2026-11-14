"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: Define a CrewAI agent
Run: python 08_define_a_crewai_agent.py
"""
# Needs: pip install crewai
# (not run while building this repo, because the package was not installed there)
from crewai import Agent, Task, Crew, Process
inv = Agent(
    role="Incident investigator",
    goal="Find the likely cause using "
         "read-only checks",
    backstory="Careful SRE who quotes "
              "evidence.",
    llm="anthropic/claude-haiku-5-5")
