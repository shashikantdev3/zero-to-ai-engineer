"""Zero to AI Engineer · Security and Guardrails · Part 8 of 11
Slide: Per-category config
Run: python 04_per_category_config.py
"""
# guardrails.v7: versioned, reviewed
# severities are 0, 2, 4, 6 by default
CONTENT_SAFETY = {
    "SelfHarm": (2, "supportive_reply"),
    "Hate": (4, "refuse"),
    "Sexual": (4, "refuse"),
    "Violence": (4, "refuse"),
}
PROMPT_SHIELDS = {
    "documents": "drop_document",
    "user_prompt": "refuse",
}
