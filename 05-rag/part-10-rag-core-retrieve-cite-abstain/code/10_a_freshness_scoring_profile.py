"""Zero to AI Engineer · RAG and Vector Search · Part 10 of 26
Slide: A freshness scoring profile
Run: python 10_a_freshness_scoring_profile.py
"""
# illustrative; check the current docs
scoring_profiles = [{
    "name": "prefer-recent",
    "functions": [{
        "type": "freshness",
        "fieldName": "effective_date",
        "boost": 2,
        "interpolation": "linear",
        "freshness": {
            "boostingDuration": "P365D"},
    }],
}]
