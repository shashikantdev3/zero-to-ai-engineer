"""Zero to AI Engineer · Python · Part 6 of 25
Slide: A Client with Three Method Types
Run: python 01_a_client_with_three_method_types.py
"""
class Client:
    def __init__(self, endpoint: str):
        self._endpoint = endpoint
    @classmethod
    def from_env(cls, env: dict):
        return cls(env["ENDPOINT"])
    @property
    def endpoint(self) -> str:
        return self._endpoint
    @staticmethod
    def normalise(s: str) -> str:
        return s.strip().lower()
