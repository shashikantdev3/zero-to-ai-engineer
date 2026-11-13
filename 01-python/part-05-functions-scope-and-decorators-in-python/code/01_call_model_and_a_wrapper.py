"""Zero to AI Engineer · Python · Part 5 of 25
Slide: call_model and a wrapper
Run: python 01_call_model_and_a_wrapper.py
"""
def call_model(prompt, /, *,
        model="small", temperature=0.0,
        max_tokens=256):
    return (prompt, model,
            temperature, max_tokens)

call_model("hi", temperature=0.2)
# call_model("hi", "big") -> TypeError

def wrapper(*args, **kwargs):
    return call_model(*args, **kwargs)
