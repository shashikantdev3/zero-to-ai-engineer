"""Zero to AI Engineer · Prompting · Part 5 of 10
Slide: A Context Builder
Run: python 01_a_context_builder.py
"""
def build_context(task, user):
    return [
        # stable, cacheable prefix
        system_rules(task),
        history_summary(task, max_tok=500),
        # permission-trimmed
        top_k(task.query, user=user, k=5),
        last_tool_result(task),
    ]
