"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 9 of 28
Follow-along lab: Two centres, six points, by hand
Run: python 04_lab_two_centres_six_points_by_hand.py
"""
pts = [1, 2, 3, 10, 11, 12]
c = [1.0, 2.0]
for step in range(3):
    groups = [[], []]
    for p in pts:
        d = [abs(p - x) for x in c]
        groups[d.index(min(d))].append(p)
    c = [sum(g) / len(g) for g in groups]
    print(f"step {step+1}: centres {c}")
print("clusters:", groups)
