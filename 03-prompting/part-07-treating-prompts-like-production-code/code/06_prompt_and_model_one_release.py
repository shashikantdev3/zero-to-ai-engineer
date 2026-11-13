"""Zero to AI Engineer · Prompting · Part 7 of 10
Slide: Prompt and Model, One Release
Run: python 06_prompt_and_model_one_release.py
"""
# One release ID pins prompt and model
RELEASE = {
    "release": "triage-2026-09-r4",
    "prompt": "triage-v3",
    # changing this triggers the full eval
    "model": "claude-haiku-5-5",
}
def needs_full_eval(old, new):
    keys = ("prompt", "model")
    return any(old[k] != new[k] for k in keys)
nxt = dict(RELEASE, model="claude-sonnet-5-5")
print(needs_full_eval(RELEASE, nxt))
