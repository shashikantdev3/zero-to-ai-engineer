"""Zero to AI Engineer · Security and Guardrails · Part 11 of 11
Slide: A Feature Flag as Kill Switch
Run: python 01_a_feature_flag_as_kill_switch.py
"""
# feature flags act as kill switches
FLAGS = {"refund_tool": True}

def handle(request):
    if not FLAGS["refund_tool"]:
        return "sent to human queue"
    return "refund tool ran"

print(handle("refund order 42"))
# incident: switch the tool off
FLAGS["refund_tool"] = False
print(handle("refund order 42"))
