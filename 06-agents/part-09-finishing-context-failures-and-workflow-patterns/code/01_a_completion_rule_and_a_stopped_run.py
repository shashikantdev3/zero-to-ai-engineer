"""Zero to AI Engineer · Agents and Tools · Part 9 of 26
Slide: A completion rule and a stopped run
Run: python 01_a_completion_rule_and_a_stopped_run.py
"""
def validate_output(out):
    # schema plus business completion rules
    if out.get("evidence"):
        return []
    return ["claim without evidence"]

# the step limit fired at step eight
run = {"stopped_by_limit": True,
       "why": "step limit 8",
       "done": ["search", "read"]}
