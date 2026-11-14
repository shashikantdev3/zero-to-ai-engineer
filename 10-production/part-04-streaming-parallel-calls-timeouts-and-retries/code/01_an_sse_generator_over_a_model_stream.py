"""Zero to AI Engineer · Production and LLMOps · Part 4 of 38
Slide: An SSE generator over a model stream
Run: python 01_an_sse_generator_over_a_model_stream.py
"""
import json, anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
def sse(m):
    with client.messages.stream(
            model=MODEL, max_tokens=300,
            thinking={"type": "disabled"},
            messages=m) as stream:
        for text in stream.text_stream:
            d = json.dumps({"delta": text})
            yield f"data: {d}\n\n"
        yield "data: [DONE]\n\n"
