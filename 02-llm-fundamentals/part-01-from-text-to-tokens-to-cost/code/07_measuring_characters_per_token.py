"""Zero to AI Engineer · LLM Fundamentals · Part 1 of 18
Slide: Measuring Characters per Token
Run: python 07_measuring_characters_per_token.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
samples = {"en": "Please reset my password.",
           "hi": "कृपया मेरा पासवर्ड रीसेट करें।"}
for lang, text in samples.items():
    msgs = [{"role": "user", "content": text}]
    toks = client.messages.count_tokens(
        model=MODEL, messages=msgs
    ).input_tokens
    print(lang, round(len(text) / toks, 2))
