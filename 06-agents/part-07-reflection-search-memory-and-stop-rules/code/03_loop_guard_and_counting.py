"""Zero to AI Engineer · Agents and Tools · Part 7 of 26
Slide: Loop guard and counting
Run: python 03_loop_guard_and_counting.py
"""
def check_repeat(run, name, args):
    parsed = json.loads(args)
    canon = json.dumps(parsed, sort_keys=True)
    sig = (name, canon)
    if sig == run.last_sig:
        raise Stop("same action twice in a row")
    run.last_sig = sig

def after_call(run, actual_usd):
    run.step += 1
    run.spent_usd += actual_usd
