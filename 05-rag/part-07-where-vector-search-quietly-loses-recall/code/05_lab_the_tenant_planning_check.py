"""Zero to AI Engineer · RAG and Vector Search · Part 7 of 26
Follow-along lab: The Tenant Planning Check
Run: python 05_lab_the_tenant_planning_check.py
"""
limits = {"S1": 50, "S2": 200, "S3": 200}
tenants, envs = 30, 2
need = tenants * envs
print(f"indexes needed: {need}")
for tier, cap in limits.items():
    ok = "fits" if need <= cap else "too many"
    print(f"{tier} cap {cap}: {ok}")
n, d, b = 1_000_000, 1536, 4
gb = n * d * b / 1e9
print(f"vector bytes: {gb:.2f} GB")
