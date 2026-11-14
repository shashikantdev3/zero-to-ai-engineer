"""Zero to AI Engineer · Production and LLMOps · Part 8 of 38
Slide: One builder for every error
Run: python 09_one_builder_for_every_error.py
"""
def problem(request, status, type_, title,
            detail, retryable, headers=None):
    body = {
        "type": type_, "title": title,
        "status": status, "detail": detail,
        "correlation_id": request.state.cid,
        "retryable": retryable}
    return JSONResponse(
        body, status_code=status,
        headers=headers,
        media_type="application/problem+json")
