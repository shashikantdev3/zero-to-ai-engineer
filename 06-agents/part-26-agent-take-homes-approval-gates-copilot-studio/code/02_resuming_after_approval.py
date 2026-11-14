"""Zero to AI Engineer · Agents and Tools · Part 26 of 26
Slide: Resuming after approval
Run: python 02_resuming_after_approval.py
"""
def execute(action, key):
    return f"ran {action['tool']} with {key}"
def resume(run_id, decision):
    p = PENDING / f"{run_id}.json"
    rec = json.loads(p.read_text())
    h, act = rec["plan_hash"], rec["action"]
    bad = decision.get("plan_hash") != h
    if bad or time.time() > rec["exp"]:
        return "rejected: stale or mismatched"
    if decision.get("approved") is not True:
        return "rejected by human"
    return execute(act, f"{run_id}:{h}")
