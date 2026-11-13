"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Check the end, then validate
Run: python 07_check_the_end_then_validate.py
"""
# Note: this is a fragment from the slide. It uses names that are set up elsewhere (for example a model client),
# so on its own it stops with NameError.
class Truncated(Exception):
    pass

def full_text(final, buf):
    # refusal and content filter signals
    # are provider specific: check them here
    if final.stop_reason == "max_tokens":
        raise Truncated("hit the token limit")
    return "".join(buf)

raw = full_text(final, buf)
inv = Invoice.model_validate_json(raw)
