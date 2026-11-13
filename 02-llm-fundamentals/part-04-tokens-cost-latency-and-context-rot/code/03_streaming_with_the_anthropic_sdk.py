"""Zero to AI Engineer · LLM Fundamentals · Part 4 of 18
Slide: Streaming with the Anthropic SDK
Run: python 03_streaming_with_the_anthropic_sdk.py
"""
# Needs: pip install anthropic
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
q = "Define prefill in two lines."
msgs = [{"role": "user", "content": q}]
with client.messages.stream(
        model=MODEL, max_tokens=200,
        thinking={"type": "disabled"},
        messages=msgs) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()
print("\n", final.usage.output_tokens)
