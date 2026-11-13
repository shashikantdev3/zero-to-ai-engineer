"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Stream for display, keep a buffer
Run: python 06_stream_for_display_keep_a_buffer.py
"""
# Needs: pip install anthropic
# Note: this is a fragment from the slide. It uses names that are set up elsewhere (for example a model client),
# so on its own it stops with NameError.
import anthropic
client = anthropic.Anthropic()
MODEL = "claude-haiku-5-5"
buf = []
with client.messages.stream(
        model=MODEL, max_tokens=300,
        thinking={"type": "disabled"},
        messages=msgs) as stream:
    for text in stream.text_stream:
        # display only, never parse here
        print(text, end="")
        buf.append(text)
    final = stream.get_final_message()
