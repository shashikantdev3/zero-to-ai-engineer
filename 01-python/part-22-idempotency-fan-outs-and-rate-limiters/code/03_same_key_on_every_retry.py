"""Zero to AI Engineer · Python · Part 22 of 25
Slide: Same key on every retry
Run: python 03_same_key_on_every_retry.py
"""
import time

async def create_ticket(client, payload, key):
    # the caller saved key with the job first,
    # so a restart sends the same key again
    deadline = time.monotonic() + 60
    return await retry(
        lambda: attempt(client, payload, key),
        deadline=deadline)

# key = operation_key(req_id, "create_ticket")
# save it with the job; then call
