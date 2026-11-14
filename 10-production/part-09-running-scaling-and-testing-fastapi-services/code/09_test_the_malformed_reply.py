"""Zero to AI Engineer · Production and LLMOps · Part 9 of 38
Slide: Test the malformed reply
Run: python 09_test_the_malformed_reply.py
"""
def test_malformed_json_error_contract():
    app.dependency_overrides[llm_client] = (
        lambda: FakeLLM("not json {"))
    r = client.post("/v1/ask",
                    json={"question": "x"})
    assert r.status_code == 502
    ctype = r.headers["content-type"]
    assert ctype.startswith(PROBLEM)
    assert r.json()["retryable"] is True
