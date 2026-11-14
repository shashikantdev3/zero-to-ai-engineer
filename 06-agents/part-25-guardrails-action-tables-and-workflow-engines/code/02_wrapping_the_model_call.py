"""Zero to AI Engineer · Agents and Tools · Part 25 of 26
Slide: Wrapping the model call
Run: python 02_wrapping_the_model_call.py
"""
SAFE = ("I cannot share that. "
        "A person will follow up.")

def guarded(call_model, ins, outs, text):
    reason = first_fail(ins, text)
    if reason is not None:
        return f"Blocked: {reason}"
    reply = call_model(text)
    if first_fail(outs, reply) is not None:
        return SAFE
    return reply
