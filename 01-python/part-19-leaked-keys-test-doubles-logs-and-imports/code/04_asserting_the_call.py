"""Zero to AI Engineer · Python · Part 19 of 25
Slide: Asserting the call
Run: python 04_asserting_the_call.py
"""
from unittest.mock import Mock
def test_sends_context_at_temp_zero():
    # mock: records the call
    llm = Mock()
    llm.complete.return_value = "irrelevant"
    docs = ["leave is 20 days",
            "payroll runs monthly"]
    answer("leave policy", llm,
           FakeRetriever(docs))
    kw = llm.complete.call_args.kwargs
    assert "leave is 20 days" in kw["prompt"]
    assert kw["temperature"] == 0
