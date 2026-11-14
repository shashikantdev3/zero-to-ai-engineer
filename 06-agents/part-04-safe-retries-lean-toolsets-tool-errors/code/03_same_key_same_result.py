"""Zero to AI Engineer · Agents and Tools · Part 4 of 26
Slide: Same key, same result
Run: python 03_same_key_same_result.py
"""
# --- repeated from 01_building_the_idempotency_key.py, 02_reserve_first_then_act.py so this file runs on its own ---
import hashlib, json

def sha(text):
    return hashlib.sha256(
        text.encode()).hexdigest()

def idem_key(inc, plan, step, action, args):
    a = json.dumps(args, sort_keys=True,
                   separators=(",", ":"))
    return sha(f"{inc}:{plan}:{step}"
               f":{action}:{sha(a)}")

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

# --- this slide ---
def restart(idempotency_key):
    print("restarting")
    return {"restarted": "api"}

k_api = idem_key("INC7", "ab12", 2,
                 "restart", {"svc": "api"})
k_wrk = idem_key("INC7", "ab12", 2,
                 "restart", {"svc": "worker"})
print(k_api == k_wrk)
print(apply_change(k_api, restart))
print(apply_change(k_api, restart))
