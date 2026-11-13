"""Zero to AI Engineer · Prompting · Part 1 of 10
Slide: Building the Message List
Run: python 02_building_the_message_list.py
"""
SYSTEM_PROMPT_V3 = "Stable rules, version 3."
q = "How do I reset my password?"
docs = "Doc A: use the reset portal."
user = (f"<question>{q}</question>\n"
        f"<documents>{docs}</documents>")
messages = [
    # stable rules, versioned
    {"role": "system",
     "content": SYSTEM_PROMPT_V3},
    {"role": "user", "content": user},
]
