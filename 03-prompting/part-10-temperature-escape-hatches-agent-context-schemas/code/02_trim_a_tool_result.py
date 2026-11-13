"""Zero to AI Engineer · Prompting · Part 10 of 10
Slide: Trim a tool result
Run: python 02_trim_a_tool_result.py
"""
def tool_result_for_context(
    result: str,
    ref_id: str,
    max_chars: int = 2000,
) -> str:
    if len(result) <= max_chars:
        return result
    note = (
        "\n[truncated; fetch full output"
        f" with id={ref_id}]"
    )
    return result[:max_chars] + note
