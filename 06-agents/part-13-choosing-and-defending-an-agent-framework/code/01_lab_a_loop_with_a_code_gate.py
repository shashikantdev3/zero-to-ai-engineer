"""Zero to AI Engineer · Agents and Tools · Part 13 of 26
Follow-along lab: A loop with a code gate
Run: python 01_lab_a_loop_with_a_code_gate.py
"""
runs = {}
def propose(step):
    return ["look", "look", "change"][step]
def gate(action, signed):
    return action == "look" or signed
run_id = "run-1"
runs[run_id] = {"step": 0, "log": []}
for step in range(3):
    act = propose(step)
    ok = gate(act, signed=False)
    runs[run_id]["log"].append((act, ok))
    print(f"step {step}: {act} allowed={ok}")
runs[run_id]["step"] = 3
print("resume at", runs[run_id]["step"])
