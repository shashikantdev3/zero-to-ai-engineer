# Python · Part 10 of 25: Inheritance, Descriptors and Attribute Hooks

Zero to AI Engineer, by DevWithData. Watch the video, code along, then do the homework.

Open `lesson.html` in a browser for the same lesson as a click-through page (Back, Play, Next, or the arrow keys).

## What this part covers

1. Cooperative __init__, explicit parent calls and C3 failure
2. Descriptors and attribute lookup order
3. __init_subclass__ versus metaclasses
4. __getattr__ versus __getattribute__
5. Question drill: OOP

## Key takeaways

- Everyone forwards **kwargs via super(); base runs once
- Data descriptor, instance dict, non-data, then __getattr__
- __init_subclass__ first; metaclasses for class creation
- __getattr__ for fallbacks; careful with __getattribute__
- Know the traps: explicit calls, properties, recursion

## Code in this part

| File | From the slide | Runs as is |
|---|---|---|
| `code/01_a_cooperative_diamond.py` | A cooperative diamond | yes |
| `code/02_when_c3_cannot_find_an_order.py` | When C3 cannot find an order | yes |
| `code/03_a_validating_descriptor.py` | A validating descriptor | yes |
| `code/04_using_the_descriptor.py` | Using the descriptor | yes |
| `code/05_lab_watch_the_lookup_order_happen.py` | Watch the lookup order happen | yes |
| `code/06_a_self_registering_base_class.py` | A self registering base class | yes |
| `code/07_defining_a_tool_registers_it.py` | Defining a tool registers it | yes |
| `code/08_a_forwarding_proxy.py` | A forwarding proxy | yes |

## Follow-along lab

Type it yourself, then compare your output.

`code/05_lab_watch_the_lookup_order_happen.py` prints:

```text
d -> data
n -> inst
m is m: False
```

## Pause-and-think questions

Answer before you open the answer. In the video, comment your answer with the timestamp.

**1. In a diamond where classes call their parent's init by name, how many times does the shared base run?**

- A. Twice
- B. Once, just like with super
- C. Never, it gets skipped

<details><summary>Answer</summary>

**A. Twice**. Calling Parent.__init__ by name bypasses the MRO

</details>

**2. If x is a property on the class, what does assigning one to obj dot x do?**

- A. Writes x into the instance dict
- B. Runs the setter, or raises
- C. Replaces the property on the class

<details><summary>Answer</summary>

**B. Runs the setter, or raises**. Data descriptors intercept assignment before the instance dict

</details>

**3. What happens when a class inherits from two bases with different, unrelated metaclasses?**

- A. A metaclass conflict TypeError
- B. Python merges both metaclasses
- C. The first base's metaclass wins

<details><summary>Answer</summary>

**A. A metaclass conflict TypeError**. Two unrelated metaclasses means a conflict TypeError

</details>

**4. You override getattribute to log access, and use self dot log inside it. Why do you get a RecursionError?**

- A. Logging is banned in dunder methods
- B. Reading self dot log calls it again
- C. The log attribute does not exist yet

<details><summary>Answer</summary>

**B. Reading self dot log calls it again**. Inside __getattribute__, use object.__getattribute__

</details>

**5. What should dunder eq return when it receives a type it does not understand?**

- A. False
- B. Raise a TypeError
- C. NotImplemented

<details><summary>Answer</summary>

**C. NotImplemented**. Return NotImplemented, let Python ask the other operand

</details>

## Say it in the interview

**Cooperative init in an interview**

- Take what you understand, forward the rest
- Calling a parent by name runs it twice
- Prefer shallow mixins over deep diamonds

**Descriptors in an interview**

- Descriptors sit behind property, methods and more
- Data wins over the dict, non-data loses
- Use them through property and Pydantic

**Metaclasses in an interview**

- Reach for __init_subclass__ first
- Metaclasses are for frameworks like ORMs and ABCs
- Choosing less complexity is the senior signal

**Attribute hooks in an interview**

- __getattr__ is the fallback for proxies
- Override __getattribute__ only via object's version
- Unknown names must raise AttributeError

## Homework

- [ ] Run the diamond, then break it with A.__init__
- [ ] Create R(P, Q) and read the TypeError
- [ ] Try to shadow a property on an instance
- [ ] Build a plugin registry with __init_subclass__
