"""Zero to AI Engineer · Agents and Tools · Part 18 of 26
Slide: Checking the scope claim
Run: python 02_checking_the_scope_claim.py
"""
# Needs: pip install jwt
# --- repeated from 01_validating_the_token_with_pyjwt.py so this file runs on its own ---
import jwt  # PyJWT

# Use the audience and issuer really issued
AUD = "api://tickets-mcp"
ISS = ("https://login.microsoftonline.com/"
       "my-tenant/v2.0")

def verify(token, signing_key):
    return jwt.decode(
        token, key=signing_key,
        algorithms=["RS256"],
        audience=AUD, issuer=ISS)

# --- this slide ---
# Claim names differ by identity provider.
# Entra: delegated scopes in "scp" (spaces),
# app permissions in "roles" (a list).
# Others use "scope". Sample decoded claims:
claims = {"aud": AUD, "scp": "tickets.read"}
raw = claims.get("scp") or claims.get("scope")
scopes = (raw or "").split()
if "tickets.read" not in scopes:
    raise PermissionError("missing scope")
print("scope ok:", scopes)
