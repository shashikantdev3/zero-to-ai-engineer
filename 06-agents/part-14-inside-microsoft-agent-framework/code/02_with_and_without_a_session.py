"""Zero to AI Engineer · Agents and Tools · Part 14 of 26
Slide: With and without a session
Run: python 02_with_and_without_a_session.py
"""
# --- repeated from 01_a_toy_agent_with_the_real_nouns.py so this file runs on its own ---
# Toy model of the Agent Framework nouns
class Agent:
    def __init__(self, name, instr, tools):
        self.name, self.instr = name, instr
        self.tools = tools

    def run(self, text, session=None):
        if session is None:
            session = []
        session.append(text)
        n = len(session)
        return f"{self.name} sees {n} turn(s)"

# --- this slide ---
bot = Agent("investigator", "Read-only.", [])
# no session: every run starts fresh
print(bot.run("Why is api slow?"))
print(bot.run("And the worker?"))
# pass a session: memory across runs
session = []
print(bot.run("Why is api slow?", session))
print(bot.run("And the worker?", session))
