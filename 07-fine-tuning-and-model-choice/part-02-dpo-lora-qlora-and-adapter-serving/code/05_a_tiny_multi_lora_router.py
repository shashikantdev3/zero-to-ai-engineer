"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 2 of 10
Slide: A tiny multi-LoRA router
Run: python 05_a_tiny_multi_lora_router.py
"""
# one shared base, many small adapters
base = "BASE_MODEL"
adapters = {"triage": "triage-v3",
            "summary": "summary-v1"}
log = []
def serve(req_id, name):
    release = adapters[name]
    log.append((req_id, release))
    return f"{name} on {base}"
print(serve("r1", "triage"))
print(serve("r2", "summary"))
print(log)
