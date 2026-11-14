"""Zero to AI Engineer · Agents and Tools · Part 24 of 26
Follow-along lab: An iterations alert by hand
Run: python 03_lab_an_iterations_alert_by_hand.py
"""
import statistics as st
last = [4, 5, 5, 6, 4, 5, 7]
this = [6, 7, 7, 8, 6, 7, 9]
p50_old = st.median(last)
p50_new = st.median(this)
rise = (p50_new - p50_old) / p50_old * 100
print(f"p50 last week: {p50_old}")
print(f"p50 this week: {p50_new}")
print(f"rise: {rise:.0f} percent")
errors = 0
print(f"errors: {errors}")
print("ALERT" if rise > 30 else "ok")
