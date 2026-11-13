# Setup

## 1. Python

Use Python 3.12 or newer. A virtual environment keeps things clean:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS or Linux: source .venv/bin/activate
```

Most files in this repo use only the standard library and need nothing else.

## 2. Files that call a model

Some lessons call a model. Those files use the Anthropic Python SDK.

```bash
pip install anthropic
```

Put your key in an environment variable. The code reads it from there.

```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "paste-your-key-here"
# macOS or Linux
export ANTHROPIC_API_KEY="paste-your-key-here"
```

Three rules for keys:

1. Never type a key into a code file.
2. Never print a key, and never paste one into a chat, a screenshot or a commit.
3. If a key leaks, revoke it and create a new one. Deleting the line is not enough.

## 3. Using OpenAI or Gemini instead

The ideas in this series are the same on every provider. Set that provider's key in its own environment variable, then change the client call.

**Anthropic (used in this series)**

```python
import anthropic

client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY
resp = client.messages.create(
    model="claude-haiku-5-5", max_tokens=200,
    thinking={"type": "disabled"},
    messages=[{"role": "user", "content": "Say hello."}])
print(resp.content[0].text)
```

Why `thinking` is switched off: by default a Claude reply can start with a thinking block, so the first block is not always the text. The simple examples in this series switch thinking off on the small model and read the first block. The examples about reasoning effort leave it on and join the text blocks instead.

**OpenAI** (`pip install openai`)

```python
from openai import OpenAI

client = OpenAI()                        # reads OPENAI_API_KEY
resp = client.chat.completions.create(
    model=OPENAI_MODEL,
    messages=[{"role": "user", "content": "Say hello."}])
print(resp.choices[0].message.content)
```

**Gemini** (`pip install google-genai`)

```python
from google import genai

client = genai.Client()                  # reads GEMINI_API_KEY or GOOGLE_API_KEY
resp = client.models.generate_content(model=GEMINI_MODEL, contents="Say hello.")
print(resp.text)
```

Set `OPENAI_MODEL` or `GEMINI_MODEL` to a current model name from that provider's model list.

Two honest notes:

- Every Anthropic file in this repo was run while the repo was built. The OpenAI and Gemini snippets above follow the standard pattern of those SDKs and were not run here.
- Current Claude models do not accept `temperature`, `top_p` or `top_k`. OpenAI and Gemini do. Where a lesson is about those settings, the code here shows the idea with a small offline simulation, so it runs without any key.
