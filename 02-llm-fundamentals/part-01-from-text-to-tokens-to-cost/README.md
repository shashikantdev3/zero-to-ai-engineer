# LLM Fundamentals · Part 1 of 18: From Text to Tokens to Cost

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Large language model (next-token prediction)
2. Tokens and tokenisation
3. Byte pair encoding (BPE)
4. The four-characters rule and non-English cost

## Key takeaways

- Predict, sample, append, repeat
- Everything is counted in tokens
- BPE: merge frequent pairs, no grammar
- Rule of thumb for sketches, measure for budgets

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_toy_model_and_sampler.py` | A Toy Model and Sampler | yes |
| `code/02_running_the_loop.py` | Running the Loop | yes |
| `code/03_counting_tokens_with_the_api.py` | Counting Tokens With the API | yes |
| `code/04_finding_the_top_pair.py` | Finding the Top Pair | yes |
| `code/05_merging_the_pair.py` | Merging the Pair | yes |
| `code/06_lab_lab_train_a_tiny_bpe.py` | Lab: Train a Tiny BPE | yes |
| `code/07_measuring_characters_per_token.py` | Measuring Characters per Token | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/06_lab_lab_train_a_tiny_bpe.py` prints:

```text
merge l+o seen 4 times
merge lo+w seen 4 times
merge low+e seen 2 times
low | lowe r | lowe s t | s low
```

## Try it without a key

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer): Paste text and see how it splits into tokens. Free. It may ask you to sign in; no payment is needed.
- [Tiktokenizer](https://tiktokenizer.vercel.app): Token counts for several models side by side. Free, no account.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does the same prompt always give the same answer?**

- A. Yes, same prompt means same output
- B. No, it samples from a distribution
- C. Only after the model is retrained

<details><summary>Answer</summary>

**B. No, it samples from a distribution**. Output is sampled, so the same prompt can vary

</details>

**2. Why does a 10-word Hindi sentence cost more than a 10-word English one?**

- A. Providers add a fee for Hindi
- B. Hindi words take longer to read
- C. Hindi words split into more tokens

<details><summary>Answer</summary>

**C. Hindi words split into more tokens**. You pay per token, not per word

</details>

**3. Why can't a model reliably count the r's in strawberry?**

- A. It sees subword tokens, not letters
- B. Its vocabulary has no letter r
- C. BPE splits words by syllables

<details><summary>Answer</summary>

**A. It sees subword tokens, not letters**. BPE is pure frequency, and the model sees tokens

</details>

**4. Users write in Hindi and paste JSON logs. Is a 4-chars-per-token budget safe?**

- A. No, measure real traffic per language
- B. Yes, the rule fits all text
- C. Yes, if you add five percent

<details><summary>Answer</summary>

**A. No, measure real traffic per language**. Four characters is a sketch, not a contract

</details>

## Say it in the interview

**Say It: Next-Token Prediction**

- An LLM is a next-token predictor.
- Sampled output means answers can vary.
- Plausible is not true. Ground and check.

**Say It: Tokens**

- The model sees token IDs, not words.
- Tokens drive cost, limits, and behaviour.
- Count with that model's own tokenizer.

**Say It: Byte Pair Encoding**

- Start from bytes, merge the top pair, repeat.
- Byte-level BPE encodes anything.
- Rare languages and domains cost more tokens.

**Say It: The Four-Character Rule**

- Four characters is only a first sketch.
- JSON, code, and Hindi cost more.
- Measure real traffic, per language.

## Homework

- [ ] Run the toy loop twice, compare outputs
- [ ] Count tokens: a sentence versus a code
- [ ] Run the BPE lab with your own words
- [ ] Measure chars per token in two languages
