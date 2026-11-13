"""Zero to AI Engineer · Python · Part 18 of 25
Follow-along lab: Script a failure, then a success
Run: python 05_lab_script_a_failure_then_a_success.py
"""
from unittest.mock import Mock
class RateLimited(Exception): ...
def ask(client, text):
    for i in range(3):
        try:
            return client.complete(prompt=text)
        except RateLimited:
            if i == 2:
                raise
c = Mock()
c.complete.side_effect = [RateLimited(), "ok"]
print("reply:", ask(c, "hi"))
print("calls:", c.complete.call_count)
print("args:", c.complete.call_args.kwargs)
