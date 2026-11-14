"""Zero to AI Engineer · Agents and Tools · Part 16 of 26
Follow-along lab: Simulate a retry storm
Run: python 03_lab_simulate_a_retry_storm.py
"""
users = 100
sdk = 3
chain = 3
app = 2
print("one layer:", sdk)
print("two layers:", sdk * chain)
print("three layers:", sdk * chain * app)
storm = users * sdk * chain * app
print("100 users, 3 layers:", storm)
print("100 users, 1 layer:", users * sdk)
