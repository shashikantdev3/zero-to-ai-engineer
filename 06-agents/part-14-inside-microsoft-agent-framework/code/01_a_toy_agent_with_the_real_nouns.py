"""Zero to AI Engineer · Agents and Tools · Part 14 of 26
Slide: A toy agent with the real nouns
Run: python 01_a_toy_agent_with_the_real_nouns.py
"""
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
