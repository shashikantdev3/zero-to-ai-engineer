"""Zero to AI Engineer · Prompting · Part 7 of 10
Slide: A Versioned Prompt Record
Run: python 03_a_versioned_prompt_record.py
"""
# prompts/triage/v3 as a Python record
TRIAGE_V3 = {
    "id": "triage-v3",
    "model": "claude-haiku-5-5",
    "max_tokens": 200,
    "system": "TASK: Classify an IT "
              "support ticket...",
}
def log_call(req_id, p):
    print(req_id, p["id"], p["model"],
          p["max_tokens"])
log_call("req-17", TRIAGE_V3)
