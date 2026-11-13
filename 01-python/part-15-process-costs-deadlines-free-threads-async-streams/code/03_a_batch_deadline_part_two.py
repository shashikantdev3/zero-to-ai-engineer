"""Zero to AI Engineer · Python · Part 15 of 25
Slide: A Batch Deadline, Part Two
Run: python 03_a_batch_deadline_part_two.py
"""
def split(tasks, done, pending):
    ok, failed = [], []
    for t in done:
        i = tasks[t]
        if t.cancelled():
            failed.append((i, "cancelled"))
        elif t.exception() is not None:
            failed.append((i, t.exception()))
        else:
            ok.append((i, t.result()))
    timed_out = [tasks[t] for t in pending]
    return ok, failed, timed_out
