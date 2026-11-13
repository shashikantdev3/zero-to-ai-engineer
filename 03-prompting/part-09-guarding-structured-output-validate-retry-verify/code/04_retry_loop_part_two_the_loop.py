"""Zero to AI Engineer · Prompting · Part 9 of 10
Slide: Retry loop, part two: the loop
Run: python 04_retry_loop_part_two_the_loop.py
"""
def extract(text, max_attempts=3):
    msgs = [{"role": "user", "content": text}]
    check = Invoice.model_validate_json
    for _ in range(max_attempts):
        raw = llm(msgs)
        try:
            inv = check(raw)
        except ValidationError as e:
            msgs += fix_request(raw, e)
            continue
        return check_truth(inv, text)
    raise NeedsHumanReview("still invalid")
