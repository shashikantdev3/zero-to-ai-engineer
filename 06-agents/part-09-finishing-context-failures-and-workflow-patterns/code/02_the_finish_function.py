"""Zero to AI Engineer · Agents and Tools · Part 9 of 26
Slide: The finish function
Run: python 02_the_finish_function.py
"""
# --- repeated from 01_a_completion_rule_and_a_stopped_run.py so this file runs on its own ---
def validate_output(out):
    # schema plus business completion rules
    if out.get("evidence"):
        return []
    return ["claim without evidence"]

# the step limit fired at step eight
run = {"stopped_by_limit": True,
       "why": "step limit 8",
       "done": ["search", "read"]}

# --- this slide ---
def finish(run, out):
    errs = validate_output(out)
    if errs or run["stopped_by_limit"]:
        return {
            "status": "incomplete",
            "completed": run["done"],
            "missing": errs or [run["why"]],
            "escalated_to": "on-call"}
    return {"status": "complete",
            "result": out}

print(finish(run, {"answer": "ok"}))
