"""Zero to AI Engineer · Agents and Tools · Part 3 of 26
Slide: Exchange the token on behalf of
Run: python 02_exchange_the_token_on_behalf_of.py
"""
# Needs: pip install msal
# (not run while building this repo, because the package was not installed there)
# --- repeated from 01_build_the_confidential_client.py so this file runs on its own ---
import os
import msal
AUTH = "https://login.microsoftonline.com/"
tenant = os.environ["TENANT_ID"]
client_id = os.environ["CLIENT_ID"]
# production: certificate or federated cred
cred = os.environ["CLIENT_CRED"]
cca = msal.ConfidentialClientApplication(
    client_id,
    authority=AUTH + tenant,
    client_credential=cred)

# --- this slide ---
# the token the user sent to your API
user_token = os.environ.get("USER_TOKEN", "")
# delegated scope, smallest needed
G = "https://graph.microsoft.com/"
SCOPE = G + "User.Read"
result = cca.acquire_token_on_behalf_of(
    user_assertion=user_token,
    scopes=[SCOPE])
print("access_token" in result)
