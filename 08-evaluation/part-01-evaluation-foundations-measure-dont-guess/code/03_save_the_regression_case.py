"""Zero to AI Engineer · Evaluation · Part 1 of 11
Slide: Save the regression case
Run: python 03_save_the_regression_case.py
"""
def add_case(trace, doc_ids, ftype, path):
    # path: access-controlled eval storage
    q = redact(trace["user_query"])
    case = {
        "id": f"reg-{trace['trace_id']}",
        "question": q,
        "expected_doc_ids": doc_ids,
        "failure_type": ftype,
        "source": "production_incident",
    }
    with open(path, "a") as f:
        f.write(json.dumps(case) + "\n")
