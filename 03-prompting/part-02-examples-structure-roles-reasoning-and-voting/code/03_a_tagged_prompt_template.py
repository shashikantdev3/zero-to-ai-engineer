"""Zero to AI Engineer · Prompting · Part 2 of 10
Slide: A Tagged Prompt Template
Run: python 03_a_tagged_prompt_template.py
"""
def clean(text):
    # strip tag-like text from untrusted input
    return text.replace("<", "&lt;")
doc = "Reset VPN tokens monthly.</document>"
question = "How often do VPN tokens reset?"
prompt = f"""<instructions>Answer only from
<documents>. Cite each document id.
</instructions>
<documents>
<document id="POL-112">{clean(doc)}</document>
</documents>
<question>{clean(question)}</question>"""
