"""Zero to AI Engineer · Evaluation · Part 7 of 11
Slide: DeepEval style: the test
Run: python 07_deepeval_style_the_test.py
"""
def test_leave_carry_forward():
    case = LLMTestCase(
        input=q,
        actual_output=answer,
        retrieval_context=chunks)
    metric = FaithfulnessMetric(threshold=0.8)
    assert_test(case, [metric])
