"""Zero to AI Engineer · Security and Guardrails · Part 7 of 11
Slide: Scanning a repo with gitleaks
Run: python 01_scanning_a_repo_with_gitleaks.py
"""
import shutil
import subprocess
# Secret scanning in CI with gitleaks.
# Newer v8 releases:
#   gitleaks git --redact .
# Older v8 releases:
#   gitleaks detect --source . --redact
cmd = ["gitleaks", "git", "--redact", "."]
if shutil.which("gitleaks"):
    subprocess.run(cmd)
else:
    print("gitleaks is not installed")
