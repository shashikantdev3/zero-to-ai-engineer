"""Zero to AI Engineer · Agents and Tools · Part 1 of 26
Slide: The argument schema
Run: python 06_the_argument_schema.py
"""
args_schema = {
    "type": "object",
    "properties": {
        "service": {"type": "string",
            "enum": ["api", "worker",
                     "scheduler"]},
        "reason": {"type": "string",
                   "maxLength": 300},
    },
    "required": ["service", "reason"],
    "additionalProperties": False,
}
