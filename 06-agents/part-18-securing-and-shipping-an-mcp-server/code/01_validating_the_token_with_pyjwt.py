"""Zero to AI Engineer · Agents and Tools · Part 18 of 26
Slide: Validating the token with PyJWT
Run: python 01_validating_the_token_with_pyjwt.py
"""
# Needs: pip install jwt
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
