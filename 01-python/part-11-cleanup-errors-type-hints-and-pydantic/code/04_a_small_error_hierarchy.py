"""Zero to AI Engineer · Python · Part 11 of 25
Slide: A Small Error Hierarchy
Run: python 04_a_small_error_hierarchy.py
"""
class LLMError(Exception): ...

class Retryable(LLMError):
    def __init__(
        self, msg: str,
        retry_after: float | None = None,
    ):
        super().__init__(msg)
        self.retry_after = retry_after

class BadRequest(LLMError): ...
