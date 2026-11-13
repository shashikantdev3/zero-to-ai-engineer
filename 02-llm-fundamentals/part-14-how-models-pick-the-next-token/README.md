# LLM Fundamentals · Part 14 of 18: How Models Pick the Next Token

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Greedy decoding and beam search
2. Temperature
3. Top-k
4. Top-p (nucleus sampling)
5. Frequency and presence penalties

## Key takeaways

- Most probable text is not most natural
- Temperature controls variety, not intelligence
- Top-k: fixed count, does not adapt
- Top-p: probability mass, adapts to confidence
- Penalties fight repetition; zero for JSON

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_greedy_versus_beam_offline.py` | Greedy Versus Beam, Offline | yes |
| `code/02_softmax_with_a_temperature.py` | Softmax With a Temperature | yes |
| `code/03_lab_print_the_temperature_table.py` | Print the Temperature Table | yes |
| `code/04_a_top_k_filter.py` | A Top-k Filter | yes |
| `code/05_a_top_p_filter.py` | A Top-p Filter | yes |
| `code/06_penalties_simulated_offline.py` | Penalties, Simulated Offline | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_print_the_temperature_table.py` prints:

```text
0 [1.0, 0.0, 0.0]
0.5 [0.864, 0.117, 0.019]
1.0 [0.659, 0.242, 0.099]
2.0 [0.502, 0.304, 0.194]
```

## Try it without a key

- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): A small GPT-2 running in your browser. Type a prompt, move the temperature slider and watch the next-token probabilities change. Free, no account.
- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Does beam search always give better answers?**

- A. Yes, as long as you use four beams
- B. Yes, it maximises total probability
- C. No, open text turns generic and repetitive

<details><summary>Answer</summary>

**C. No, open text turns generic and repetitive**. Most probable text is not most natural text

</details>

**2. Does a higher temperature make the model smarter and more creative?**

- A. Yes, up to about 1.8
- B. No, it only changes variety
- C. Yes, it explores better ideas

<details><summary>Answer</summary>

**B. No, it only changes variety**. Temperature controls variety, not intelligence

</details>

**3. Are top-k and top-p the same thing?**

- A. Yes, they are just different names
- B. No, only top-p adapts to confidence
- C. Yes, both keep k tokens

<details><summary>Answer</summary>

**B. No, only top-p adapts to confidence**. Top-k is a fixed count; top-p adapts

</details>

**4. Does top_p = 0.9 mean the model is 90% accurate?**

- A. No, it is kept probability mass
- B. Yes, nine answers in ten are right
- C. Yes, it is a confidence score

<details><summary>Answer</summary>

**A. No, it is kept probability mass**. p is kept probability mass, not accuracy

</details>

**5. Can a frequency penalty stop hallucinations?**

- A. No, it only affects repetition
- B. Yes, if set above 1.0
- C. Yes, it blocks invented facts

<details><summary>Answer</summary>

**A. No, it only affects repetition**. Penalties fight repetition, not hallucination

</details>

## Say it in the interview

**Greedy and Beam in Interviews**

- Greedy: top token each step, like T = 0
- Beam: best total, for one right answer
- In practice: temperature, top-p, validation

**Temperature in Interviews**

- Low T concentrates, high T spreads
- Variety, not intelligence or truth
- Low for extraction, higher for brainstorming

**Top-k in Interviews**

- Keep k tokens, drop the nonsense tail
- Fixed k: junk in, or good words out
- One knob at a time, judged on evals

**Top-p in Interviews**

- Smallest group reaching p, then sample
- Adapts to confidence; top-k does not
- Temperature or top-p, not both

**Penalties in Interviews**

- Presence: new topics. Frequency: fewer repeats.
- Avoid penalties for JSON and extraction
- Penalty values are not portable

## Homework

- [ ] Rerun the lab at temperature 3
- [ ] Compare top-k and top-p on one list
- [ ] Make greedy beat beam in the toy example
- [ ] Write the temperature answer in three sentences
