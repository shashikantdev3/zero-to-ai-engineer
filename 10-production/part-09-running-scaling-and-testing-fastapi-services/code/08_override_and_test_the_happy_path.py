"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: Override and test the happy path
Run: python 08_override_and_test_the_happy_path.py
"""
# Needs: pip install fastapi
# (not run while building this repo, because the package was not installed there)
from fastapi.testclient import TestClient
app.dependency_overrides[current_user] = (
    lambda: {"sub": "u1", "tid": "t1"})
client = TestClient(app)
GOOD = '{"answer":"42","citations":["doc-1"]}'
def test_ask_returns_citations():
    app.dependency_overrides[llm_client] = (
        lambda: FakeLLM(GOOD))
    r = client.post("/v1/ask",
                    json={"question": "x"})
    assert r.status_code == 200
    assert r.json()["citations"] == ["doc-1"]
