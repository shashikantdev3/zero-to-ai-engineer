"""Zero to AI Engineer · Agents and Tools · Part 12 of 26
Slide: Task, crew, kickoff
Run: python 09_task_crew_kickoff.py
"""
# Needs: pip install crewai
# (not run while building this repo, because the package was not installed there)
# --- repeated from 08_define_a_crewai_agent.py so this file runs on its own ---
from crewai import Agent, Task, Crew, Process
inv = Agent(
    role="Incident investigator",
    goal="Find the likely cause using "
         "read-only checks",
    backstory="Careful SRE who quotes "
              "evidence.",
    llm="anthropic/claude-haiku-5-5")

# --- this slide ---
task = Task(
    description="Investigate incident "
                "{incident_id}",
    expected_output="Cause with quoted "
                    "evidence",
    agent=inv)
crew = Crew(agents=[inv], tasks=[task],
            process=Process.sequential)
result = crew.kickoff(
    inputs={"incident_id": "INC-4711"})
print(result)
