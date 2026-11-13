"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Slide: A stand-in model that times out
Run: python 06_a_stand_in_model_that_times_out.py
"""
class ModelClient:
    def predict(self, features, timeout):
        raise TimeoutError("model too slow")

def rules_baseline(f):
    return 0.9 if f["amount"] > 1000 else 0.1

def log_fallback(reason):
    print("fallback:", reason)

model_client = ModelClient()
features = {"amount": 1500}
