"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Slide: Pinned config with a retirement date
Run: python 05_pinned_config_with_a_retirement_date.py
"""
from datetime import date
llm = {
    "deployment": "support-chat",
    "model_version": "<exact dated version>",
    "upgrade": "<no auto-upgrade option>",
    "retirement_date": date(2026, 3, 1),
    "change_requires": "eval_gate_pass",
}
assert llm["model_version"] != "latest"
today = date(2026, 1, 1)
left = llm["retirement_date"] - today
print("days to retirement:", left.days)
