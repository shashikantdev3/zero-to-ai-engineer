"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 24 of 28
Follow-along lab: Same Ratio, Different Verdict
Run: python 02_lab_same_ratio_different_verdict.py
"""
import math

def srm_p(n_a, n_b):
    exp = (n_a + n_b) / 2
    chi2 = ((n_a - exp) ** 2
            + (n_b - exp) ** 2) / exp
    return math.erfc(math.sqrt(chi2 / 2))

for n_a, n_b in [(480, 520),
                 (48_000, 52_000),
                 (401_600, 398_400)]:
    p = srm_p(n_a, n_b)
    print(n_a + n_b, f"p={p:.4f}",
          "SRM" if p < 0.0005 else "ok")
