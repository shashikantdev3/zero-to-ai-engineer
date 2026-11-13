"""Zero to AI Engineer · LLM Fundamentals · Part 13 of 18
Follow-along lab: Error Rate and the Slow Tail
Run: python 03_lab_error_rate_and_the_slow_tail.py
"""
r = "reset the password for account 48213"
h = "reset the password for account 48230"
rw, hw = r.split(), h.split()
wrong = sum(a != b for a, b in zip(rw, hw))
print(f"WER: {wrong / len(rw):.2f}")
ok = rw[-1] == hw[-1]
print(f"Account number right: {ok}")
ms = [300, 320, 310, 330, 305, 315, 325,
      300, 310, 1500]
avg = sum(ms) / len(ms)
print(f"Average ms: {avg:.0f}")
p95 = sorted(ms)[int(len(ms) * 0.95)]
print(f"p95 ms: {p95}")
