"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 17 of 28
Follow-along lab: Metrics by Hand, One Big Miss
Run: python 04_lab_metrics_by_hand_one_big_miss.py
"""
import math
y = [10, 12, 14, 16, 18]
p = [11, 12, 13, 17, 30]
n = len(y)
err = [a - b for a, b in zip(y, p)]
mae = sum(abs(e) for e in err) / n
rmse = math.sqrt(sum(e * e for e in err) / n)
mean = sum(y) / n
ss_res = sum(e * e for e in err)
ss_tot = sum((a - mean) ** 2 for a in y)
r2 = 1 - ss_res / ss_tot
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2:   {r2:.2f}")
