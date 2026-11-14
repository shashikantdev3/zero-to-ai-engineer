"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 10 of 10
Follow-along lab: Size a replica fleet
Run: python 04_lab_size_a_replica_fleet.py
"""
import math
# Little's law: rate times time in flight
peak_rps, secs = 20, 10
peak = peak_rps * secs
print("Peak concurrency:", peak)
kv_cap, tput_cap = 48, 40
per_rep = min(kv_cap, tput_cap)
print("Per replica:", per_rep)
n = math.ceil(peak / per_rep)
print("Replicas:", n, "+ 1 warm spare")
# Scale on waiting requests, not CPU
waiting, limit = 15, 10
print("Scale out:", waiting > limit)
