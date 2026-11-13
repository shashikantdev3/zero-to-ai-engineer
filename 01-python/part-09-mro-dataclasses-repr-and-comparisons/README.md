# Python · Part 9 of 25: MRO, Dataclasses, Repr and Comparisons

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. MRO, C3 linearisation and super()
2. dataclasses, field, frozen and __slots__
3. __str__ versus __repr__
4. Rich comparisons, NotImplemented and total_ordering
5. Choosing a container: dict, TypedDict, NamedTuple, dataclass or Pydantic

## Key takeaways

- super follows the MRO, not the parent
- Free init, repr, eq; no validation
- Containers and debuggers use repr
- NotImplemented for strangers, hash matches eq
- Validate at the boundary only

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_diamond_you_can_print.py` | A diamond you can print | yes |
| `code/02_a_frozen_retry_policy.py` | A frozen retry policy | yes |
| `code/03_ordering_on_one_field.py` | Ordering on one field | yes |
| `code/04_lab_prove_what_a_dataclass_checks.py` | Prove what a dataclass checks | yes |
| `code/05_a_chunk_with_both_views.py` | A chunk with both views | yes |
| `code/06_equality_that_steps_aside.py` | Equality that steps aside | yes |
| `code/07_sorting_with_total_ordering.py` | Sorting with total_ordering | yes |
| `code/08_typeddict_namedtuple_dataclass.py` | TypedDict, NamedTuple, dataclass | yes |
| `code/09_pydantic_at_the_boundary.py` | Pydantic at the boundary | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/04_lab_prove_what_a_dataclass_checks.py` prints:

```text
accepted: five
blocked
a: ['x'] b: []
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. For a D object, which class does the super call inside B reach?**

- A. The object class directly
- B. Class C, next in the MRO
- C. Class A, the parent B names

<details><summary>Answer</summary>

**B. Class C, next in the MRO**. super is the next class, not the parent

</details>

**2. What happens when you pass the word five as attempts to RetryPolicy?**

- A. It is accepted silently
- B. It is converted to an integer
- C. It raises a TypeError

<details><summary>Answer</summary>

**A. It is accepted silently**. Dataclasses never validate types

</details>

**3. If a class defines only dunder str, what shows when its object sits inside a list in your logs?**

- A. The default object at an address
- B. An error from the list
- C. The readable str text

<details><summary>Answer</summary>

**A. The default object at an address**. Containers use repr, so define repr

</details>

**4. Why is returning False for an unknown type a mistake in dunder eq?**

- A. False makes the object unhashable
- B. Python never tries the other operand
- C. Python raises an error instead

<details><summary>Answer</summary>

**B. Python never tries the other operand**. NotImplemented lets the other side answer

</details>

**5. Someone says to use Pydantic everywhere for safety. What is the problem?**

- A. Pydantic cannot hold nested data
- B. Pydantic models cannot be type checked
- C. No clear trust boundary, plus wasted validation

<details><summary>Answer</summary>

**C. No clear trust boundary, plus wasted validation**. One obvious boundary beats checking everywhere

</details>

## Say it in the interview

**MRO in the interview**

- MRO is the lookup order, built by C3
- super means next in this object's MRO
- Cooperate: call super, pass kwargs along

**Dataclasses in the interview**

- Dataclasses for trusted internal values
- default_factory, frozen, slots, each with a reason
- Outside data goes through Pydantic

**str and repr in the interview**

- If I write only one, it is repr
- Debuggers, tracebacks and containers use repr
- Unambiguous, and no secrets in repr

**Comparisons in the interview**

- One natural order, or a key function
- Write eq and lt, total_ordering does the rest
- NotImplemented for strangers, hash matches eq

**Containers in the interview**

- Pydantic at the boundary, dataclass inside
- Validate once, at one place
- Keys need tuple fields, not lists

## Homework

- [ ] Print the MRO of a diamond
- [ ] Hash a frozen dataclass with a list
- [ ] Write a constructor style repr
- [ ] Add total_ordering to a small class
