"""Zero to AI Engineer · Agents and Tools · Part 24 of 26
Slide: Testing the step cap
Run: python 01_testing_the_step_cap.py
"""
def run_agent(call_model, max_steps=3):
    for _ in range(max_steps):
        reply = call_model()
        if reply["type"] == "final":
            return reply["text"]
    return "Stopped: step limit, escalated"

def fake_model():
    return {"type": "tool", "name": "get_status"}

out = run_agent(fake_model, max_steps=3)
assert out.startswith("Stopped: step limit")
