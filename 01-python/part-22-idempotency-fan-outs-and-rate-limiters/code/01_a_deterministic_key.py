"""Zero to AI Engineer · Python · Part 22 of 25
Slide: A deterministic key
Run: python 01_a_deterministic_key.py
"""
import uuid

# fixed per service
NS = uuid.UUID(
    "6f1c2a52-6d3e-4a8e-9a43-2f0b5c1d7e10")

def operation_key(entity_id, operation):
    """Same operation, same key."""
    name = f"{entity_id}:{operation}"
    return str(uuid.uuid5(NS, name))

key = operation_key("r42", "create_ticket")
