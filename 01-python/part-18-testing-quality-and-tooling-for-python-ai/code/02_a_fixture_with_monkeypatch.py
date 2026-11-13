"""Zero to AI Engineer · Python · Part 18 of 25
Slide: A fixture with monkeypatch
Run: python 02_a_fixture_with_monkeypatch.py
"""
# Needs: pip install pytest
import os
import pytest

@pytest.fixture
def api_key(monkeypatch):
    monkeypatch.setenv(
        "LLM_API_KEY", "test-key")
    yield "test-key"

def test_key_is_set(api_key):
    assert os.getenv("LLM_API_KEY") == api_key
