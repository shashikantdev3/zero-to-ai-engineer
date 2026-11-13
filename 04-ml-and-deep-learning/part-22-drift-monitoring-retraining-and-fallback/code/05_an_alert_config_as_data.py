"""Zero to AI Engineer · Machine Learning and Deep Learning · Part 22 of 28
Slide: An alert config, as data
Run: python 05_an_alert_config_as_data.py
"""
alerts = {
    "data": {
        "null_rate_max": {"feature_x": 0.02},
        "freshness_hours_max": 24,
    },
    "model": {
        "positive_rate_band": [0.01, 0.05],
        "mean_confidence_drop_max": 0.05,
    },
}
print(alerts["model"])
