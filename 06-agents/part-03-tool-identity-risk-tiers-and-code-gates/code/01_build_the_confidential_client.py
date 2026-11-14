"""Zero to AI Engineer · Agents and Tools · Part 3 of 26
Slide: Build the confidential client
Run: python 01_build_the_confidential_client.py
"""
# Needs: pip install msal
# (not run while building this repo, because the package was not installed there)
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
