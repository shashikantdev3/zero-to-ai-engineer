"""Zero to AI Engineer · Production and LLMOps · Part 2 of 38
Slide: Compute cost per resolved task
Run: python 06_compute_cost_per_resolved_task.py
"""
def cost_per_resolved(token_usd, tool_usd,
                      human_min, usd_per_min,
                      resolved):
    if resolved == 0:
        # report n/a, not a fake denominator
        return None
    human = human_min * usd_per_min
    total = token_usd + tool_usd + human
    return total / resolved

print(cost_per_resolved(5, 1, 30, 2, 50))
print(cost_per_resolved(5, 1, 0, 2, 0))
