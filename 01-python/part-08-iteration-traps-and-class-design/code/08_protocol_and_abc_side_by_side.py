"""Zero to AI Engineer · Python · Part 8 of 25
Slide: Protocol and ABC side by side
Run: python 08_protocol_and_abc_side_by_side.py
"""
from abc import ABC, abstractmethod
from typing import Protocol

class LLMClient(Protocol):
    def complete(self, prompt: str) -> str:
        ...

class Retriever(ABC):
    @abstractmethod
    def search(
        self, query: str, k: int
    ) -> list[str]: ...
