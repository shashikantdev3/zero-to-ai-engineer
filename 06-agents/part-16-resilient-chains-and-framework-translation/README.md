# Agents and Tools · Part 16 of 26: Resilient Chains and Framework Translation

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. LCEL resilience: with_retry and with_fallbacks
2. Visual agent builders versus code: durability
3. Question drill: Frameworks additions
4. Framework translation table: one concept, four vocabularies

## Key takeaways

- One retry layer; eval the fallback model
- Auditable controls: versioned code or governed platform
- Pass a session; check data-plane roles
- Six concepts, four vocabularies, migrate behind evals

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_failing_model_wrapped_in_retry.py` | A failing model, wrapped in retry | after `pip install langchain-core` |
| `code/02_fallback_and_passthrough_in_a_chain.py` | Fallback and passthrough in a chain | after `pip install langchain-core` |
| `code/03_lab_simulate_a_retry_storm.py` | Simulate a retry storm | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/03_lab_simulate_a_retry_storm.py` prints:

```text
one layer: 3
two layers: 9
three layers: 18
100 users, 3 layers: 1800
100 users, 1 layer: 300
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. The SDK makes 3 attempts and LangChain makes 3. How many requests per call in a 429 storm?**

- A. Nine requests per call
- B. Three requests per call
- C. Six requests per call

<details><summary>Answer</summary>

**A. Nine requests per call**. Retries multiply across layers. Keep them in one.

</details>

**2. An interviewer says low-code is never production. Your enterprise agent runs on Copilot Studio. Best reply?**

- A. A governed platform can be production
- B. Any low-code canvas is production ready
- C. Agree, and rewrite it all in code

<details><summary>Answer</summary>

**A. A governed platform can be production**. Governed platform: fine. Ungoverned canvas: the risk.

</details>

**3. Semantic Kernel and AutoGen both went into maintenance. Agree?**

- A. Yes, both are in maintenance
- B. No, AutoGen replaced Semantic Kernel
- C. No, only AutoGen is dormant

<details><summary>Answer</summary>

**C. No, only AutoGen is dormant**. AutoGen dormant; Semantic Kernel still releases

</details>

**4. Moving a system from AutoGen to Agent Framework: is it mostly a rename?**

- A. Yes, rename the classes and ship
- B. No, migrate behind evals, one workflow
- C. Yes, once the code compiles

<details><summary>Answer</summary>

**B. No, migrate behind evals, one workflow**. Same shape, different behaviour. Migrate behind evals.

</details>

## Say it in the interview

**In the interview**

- One wrapper: with_retry and with_fallbacks
- Retry in one layer, or face a retry storm
- The fallback must pass the same golden set

**In the interview**

- Builders for proof; careful with governed workflows
- Canvas-only controls cannot be tested or versioned
- Speed and governance, against control

**In the interview**

- Translate: six concepts every framework shares
- Map LangGraph to Agent Framework, concept by concept
- Verify names; migrate one concept at a time

## Homework

- [ ] Rerun the lab with your own retry counts
- [ ] Find your SDK's default max retries
- [ ] List the six concepts with LangGraph names
- [ ] Rehearse the builder answer in thirty seconds
