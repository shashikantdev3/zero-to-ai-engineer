# Prompting · Part 2 of 10: Examples, Structure, Roles, Reasoning and Voting

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Zero-shot and few-shot examples
2. Delimiters and prompt structure
3. Role prompting
4. Chain of thought
5. Self-consistency

## Key takeaways

- Few, diverse examples; watch cost and label bias
- Tags organise; they do not defend
- Roles change style, not skill
- Reason first, but do not trust it as proof
- Agreement is a signal, not accuracy

## Code in this part

Some files here call a model. They need `pip install anthropic` and your key in the `ANTHROPIC_API_KEY` environment variable. See [SETUP.md](../../SETUP.md) for the steps, and for the same call with OpenAI or Gemini.

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_building_few_shot_messages.py` | Building Few-Shot Messages | yes |
| `code/02_sending_the_examples.py` | Sending the Examples | yes |
| `code/03_a_tagged_prompt_template.py` | A Tagged Prompt Template | yes |
| `code/04_a_role_line_in_practice.py` | A Role Line in Practice | yes |
| `code/05_reasoning_field_comes_first.py` | Reasoning Field Comes First | yes |
| `code/06_read_the_label_hide_the_rest.py` | Read the Label, Hide the Rest | yes |
| `code/07_one_classifier_call.py` | One Classifier Call | yes |
| `code/08_five_votes_and_a_threshold.py` | Five Votes and a Threshold | yes |
| `code/09_lab_vote_then_check_the_truth.py` | Vote, Then Check the Truth | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/09_lab_vote_then_check_the_truth.py` prints:

```text
noisy: network 3/5 human
  correct: True
stable: other 5/5 auto
  correct: False
```

## Try it without a key

- [Google AI Studio](https://aistudio.google.com): A real model with temperature, top-p, thinking level and output length controls. Needs a Google account, no credit card. Do not paste private data: free-tier prompts may be used to improve Google products.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. Is adding more few-shot examples always better?**

- A. Only when the model is small
- B. Yes, more examples always help
- C. No, cost rises and skew biases labels

<details><summary>Answer</summary>

**C. No, cost rises and skew biases labels**. Each example costs every call, and skew biases labels

</details>

**2. Does fencing documents in tags prevent prompt injection?**

- A. Only with Markdown headings
- B. No, tags are hygiene, not defence
- C. Yes, tags block injection

<details><summary>Answer</summary>

**B. No, tags are hygiene, not defence**. Tags organise. They do not defend.

</details>

**3. Does calling the model an expert make it more accurate?**

- A. Usually little, so measure it
- B. Only for legal questions
- C. Yes, the role adds expertise

<details><summary>Answer</summary>

**A. Usually little, so measure it**. Roles change style. Measure any accuracy claim.

</details>

**4. Does the chain of thought explain why the model decided?**

- A. Not guaranteed, it may be post-hoc
- B. Yes, it is the true record
- C. Only with reasoning models

<details><summary>Answer</summary>

**A. Not guaranteed, it may be post-hoc**. Written reasoning is not an audit trail

</details>

**5. If five of five samples agree, is the answer correct?**

- A. Yes, majority means correct
- B. Not necessarily, stable can be wrong
- C. Only with ten or more runs

<details><summary>Answer</summary>

**B. Not necessarily, stable can be wrong**. Stability and accuracy are measured separately

</details>

## Say it in the interview

**Say It in the Interview**

- Zero-shot first, then three to five examples
- Diverse, tricky, other, real-looking
- Vary order, check label distribution

**Say It in the Interview**

- Named tags separate rules from data
- Hygiene, not security

**Say It in the Interview**

- Role sets tone, not accuracy
- A role cannot supply missing context

**Say It in the Interview**

- Steps become context for the next
- Use it where evals show a gain
- Reasoning models already reason internally

**Say It in the Interview**

- Sample several times, take the majority
- Low agreement routes to a human
- Consistently wrong still agrees

## Homework

- [ ] Add three examples, including an other case
- [ ] Tag a document and escape closing tags
- [ ] Put a reasoning field before the label
- [ ] Rerun the lab with your own labels
