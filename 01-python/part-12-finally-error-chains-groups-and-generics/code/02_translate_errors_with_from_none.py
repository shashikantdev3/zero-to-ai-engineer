"""Zero to AI Engineer · Python · Part 12 of 25
Slide: Translate errors with from None
Run: python 02_translate_errors_with_from_none.py
"""
def lookup(cfg: dict, key: str) -> str:
    try:
        return cfg[key]
    except KeyError:
        # hide the inner detail
        raise LookupError(
            f"missing config {key!r}"
        ) from None
