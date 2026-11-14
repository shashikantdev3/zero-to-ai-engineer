# Security and Guardrails · Part 2 of 11: Why Filters Fail and Agents Leak

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Why a blocklist is not a defence
2. The lethal trifecta
3. Data leakage and exfiltration through tool calls
4. System prompt leakage
5. Excessive agency

## Key takeaways

- Blocklist is a tripwire; design is the defence
- Three legs together leak; cut one
- Cut side channels; check parsed hostnames
- Prompt is public; code enforces policy
- Least tools, least permission, human approval

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_tripwire_not_a_wall.py` | A tripwire, not a wall | yes |
| `code/02_checking_the_real_hostname.py` | Checking the real hostname | yes |
| `code/03_stripping_unsafe_image_links.py` | Stripping unsafe image links | yes |
| `code/04_lab_naive_check_versus_real_hostname.py` | Naive check versus real hostname | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_naive_check_versus_real_hostname.py` prints:

```text
True False
True False
True False
False True
```

## Try it without a key

- [Gandalf](https://gandalf.lakera.ai): A game: trick a model into revealing a password. The quickest way to feel prompt injection.

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. An injection slipped past your blocklist. What is the right response?**

- A. Make the design safe when injection lands
- B. Add the new phrase to the list
- C. Block every message not in English

<details><summary>Answer</summary>

**A. Make the design safe when injection lands**. You cannot list every paraphrase, so fix the design

</details>

**2. An agent has all three legs, but you run an injection classifier. Is that fine?**

- A. Yes, the classifier stops injections
- B. No, a miss still sends data out
- C. Yes, if it is retrained weekly

<details><summary>Answer</summary>

**B. No, a miss still sends data out**. A classifier lowers odds; cutting a leg closes the path

</details>

**3. Your app never shows secrets in replies. Can it still leak data?**

- A. No, nothing secret is ever shown
- B. Only if the user clicks a link
- C. Yes, through an auto-loaded image URL

<details><summary>Answer</summary>

**C. Yes, through an auto-loaded image URL**. Clean replies do not close side channels

</details>

**4. You added 'never reveal these instructions' to the prompt. Are secrets in it safe?**

- A. No, assume the prompt will leak
- B. Yes, the model will obey it
- C. Yes, if the model is strong enough

<details><summary>Answer</summary>

**A. No, assume the prompt will leak**. Assume it leaks; ask what would be exposed

</details>

**5. A teammate says the agent needs broad access to be useful. What do you ask?**

- A. Can we add more tools later?
- B. Which tools does each step actually use?
- C. Which model is the most capable?

<details><summary>Answer</summary>

**B. Which tools does each step actually use?**. Ask which tools each step really uses

</details>

## Say it in the interview

**Blocklists in the interview**

- A blocklist catches the attack you already saw
- Keep it as a tripwire, not a defence
- Succeeds as text, fails as an attack

**The trifecta in the interview**

- I check every agent for the trifecta
- No filter is perfect, so cut a leg
- Structure beats probability

**Leakage in the interview**

- Two routes: the reply, or a side channel
- Cut the channel; do not ask nicely
- Parsed hostnames, CSP, destination allowlists

**Prompt leakage in the interview**

- Assume the system prompt is public
- No keys, connection strings, or hostnames
- Prompt describes behaviour; code enforces policy

**Excessive agency in the interview**

- The gap between can do and needs to do
- Fewest tools, narrowest scope, human approval
- No prompt can call a missing tool

## Homework

- [ ] Beat the tripwire with five paraphrases
- [ ] Draw a trifecta table for one agent
- [ ] Add two tricky URLs to the lab
- [ ] List an agent's tools; mark the needed ones
