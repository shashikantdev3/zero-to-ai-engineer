"""Zero to AI Engineer · Agents and Tools · Part 4 of 26
Slide: Reserve first, then act
Run: python 02_reserve_first_then_act.py
"""
store = {}

def apply_change(key, do):
    rec = {"status": "pending"}
    # atomic reserve: insert if absent
    if store.setdefault(key, rec) is not rec:
        old = store[key]
        if old["status"] == "done":
            return old["result"]
        return {"status": "in_progress"}
    result = do(idempotency_key=key)
    rec.update(status="done", result=result)
    return result
