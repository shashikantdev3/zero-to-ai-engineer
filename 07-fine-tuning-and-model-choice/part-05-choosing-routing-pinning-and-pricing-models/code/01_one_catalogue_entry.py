"""Zero to AI Engineer · Fine-tuning and Model Choice · Part 5 of 10
Slide: One catalogue entry
Run: python 01_one_catalogue_entry.py
"""
entry = {
    "id": "chat-small-v3",
    "model": "<exact pinned version>",
    "regions": ["eu", "india"],
    "data_class_max": "confidential",
    "golden_set_pass": True,
    "retirement": "<date from provider>",
    "owner": "platform-team",
}
ok = "eu" in entry["regions"]
print(entry["id"], "allowed in eu:", ok)
