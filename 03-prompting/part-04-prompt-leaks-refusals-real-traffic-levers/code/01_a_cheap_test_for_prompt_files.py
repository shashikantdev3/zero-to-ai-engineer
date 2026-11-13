"""Zero to AI Engineer · Prompting · Part 4 of 10
Slide: A Cheap Test for Prompt Files
Run: python 01_a_cheap_test_for_prompt_files.py
"""
# Cheap extra check, not the real control
import pathlib, re
SECRET = re.compile(
    r"(api[_-]?key|password|secret"
    r"|connection[_-]?string)\s*[:=]",
    re.I)
def test_prompts_hold_no_secrets():
    root = pathlib.Path("prompts")
    for p in root.rglob("*"):
        if p.is_file():
            t = p.read_text(errors="ignore")
            assert not SECRET.search(t), p
