"""Zero to AI Engineer · Agents and Tools · Part 8 of 26
Slide: Building a six block prompt
Run: python 03_building_a_six_block_prompt.py
"""
prompt = {
    "IDENTITY": "IT operations investigator",
    "CAPABILITIES": "health, logs, deploys",
    "BOUNDARIES": "never claim a cause"
        " without quoted evidence",
    "POLICY": "check deploys before restart",
    "UNCERTAINTY": "2 failures: stop, report",
    "OUTPUT": "JSON, Finding schema",
}
system = "\n".join(
    f"[{k}] {v}" for k, v in prompt.items())
print(system)
