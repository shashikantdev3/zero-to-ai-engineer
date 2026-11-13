# Prompting · Part 5 of 10: Context Engineering: What the Model Sees

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Context engineering
2. Context window and token budget
3. Lost in the middle
4. What stays out
5. Retrieve, don't dump

## Key takeaways

- Choose what the model sees, every call
- Budget per section, enforced with explicit checks
- Fewer chunks, best one next to question
- Keep restricted data and secrets out
- Retrieve a few chunks, don't dump

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_context_builder.py` | A Context Builder | yes |
| `code/02_counting_tokens.py` | Counting Tokens | yes |
| `code/03_fitting_the_budget.py` | Fitting the Budget | yes |
| `code/04_lab_lab_trim_to_a_budget.py` | Lab: Trim to a Budget | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_lab_trim_to_a_budget.py` prints:

```text
room for docs: 106
dropped doc of 80 tokens
kept 2 docs, 90 tok
```

## Try it without a key

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer): Paste text and see how it splits into tokens. Free. It may ask you to sign in; no payment is needed.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Is context engineering just a new name for prompting?**

- A. Only for agents with tools
- B. No, it is system design
- C. Yes, same skill, new label

<details><summary>Answer</summary>

**B. No, it is system design**. Wording is prompting. Choosing the context is design.

</details>

**2. The window is a million tokens. Does your budget still matter?**

- A. No, the big window covers it
- B. Only on reasoning models
- C. Yes, cost and latency grow

<details><summary>Answer</summary>

**C. Yes, cost and latency grow**. A bigger window does not make tokens free.

</details>

**3. Should you send all fifty chunks and let the model find it?**

- A. No, send fewer, reranked chunks
- B. Yes, if the window is large
- C. Yes, the model reads everything

<details><summary>Answer</summary>

**A. No, send fewer, reranked chunks**. Fit in the window does not mean used well.

</details>

**4. Is telling the model not to reveal restricted documents enough?**

- A. Yes, if the instruction is clear
- B. No, keep them out of context
- C. Yes, with a strong system prompt

<details><summary>Answer</summary>

**B. No, keep them out of context**. Restricted data should never enter the context.

</details>

**5. Models read a million tokens now. Is RAG dead?**

- A. No, cost, freshness and permissions remain
- B. Yes, long context replaces it
- C. Yes, prompt caching replaces it

<details><summary>Answer</summary>

**A. No, cost, freshness and permissions remain**. Long context does not solve permissions or cost.

</details>

## Say it in the interview

**Say It in the Interview**

- On every call, what does the model see?
- Rules, key documents, summary, latest tool result.
- The window is a budget I spend deliberately.

**Say It in the Interview**

- My own budget matters more than the window.
- Stateless APIs resend and rebill history.
- Trim documents first, raise if it won't fit.

**Say It in the Interview**

- Long context is not used equally.
- Fewer chunks, strongest last, instruction near end.

**Say It in the Interview**

- If it is in context, it can leak.
- Filter at retrieval. No keys. Drop old dumps.

**Say It in the Interview**

- Dumping pays for everything and ignores permissions.
- Cited chunks. Update the index, not the prompt.
- Caching cuts cost, not permission or freshness risk.

## Homework

- [ ] List what your app sends per call
- [ ] Set a token budget per section
- [ ] Put the best chunk before the question
- [ ] Find one thing that should stay out
