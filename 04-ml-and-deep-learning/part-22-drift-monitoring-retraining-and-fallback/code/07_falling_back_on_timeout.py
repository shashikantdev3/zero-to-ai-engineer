"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Slide: Falling back on timeout
Run: python 07_falling_back_on_timeout.py
"""
# --- repeated from 06_a_stand_in_model_that_times_out.py so this file runs on its own ---
class ModelClient:
    def predict(self, features, timeout):
        raise TimeoutError("model too slow")

def rules_baseline(f):
    return 0.9 if f["amount"] > 1000 else 0.1

def log_fallback(reason):
    print("fallback:", reason)

model_client = ModelClient()
features = {"amount": 1500}

# --- this slide ---
try:
    score = model_client.predict(
        features, timeout=0.2)
except (TimeoutError, ConnectionError):
    score = rules_baseline(features)
    log_fallback(reason="model_unavailable")
print(score)
