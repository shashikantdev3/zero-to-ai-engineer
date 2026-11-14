"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: Keep paths inside a base folder
Run: python 08_keep_paths_inside_a_base_folder.py
"""
from pathlib import Path

BASE = Path("/srv/runbooks").resolve()

def check_path(name: str) -> Path:
    p = (BASE / name).resolve()
    if not p.is_relative_to(BASE):
        # blocks ../../etc/passwd
        raise ValueError("path outside base")
    return p
