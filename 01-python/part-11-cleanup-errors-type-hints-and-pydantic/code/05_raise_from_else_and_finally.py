"""Zero to AI Engineer · Python · Part 11 of 25
Slide: raise from, else and finally
Run: python 05_raise_from_else_and_finally.py
"""
def parse(status: int, body: str) -> str:
    try:
        if status == 429:
            raise Retryable("rate limit", 2.0)
        if status >= 400:
            raise BadRequest(body)
        result = body.strip()
    except KeyError as e:
        raise BadRequest("malformed") from e
    else:
        return result
    finally: pass  # cleanup and metrics
