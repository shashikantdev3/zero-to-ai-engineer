"""Zero to AI Engineer · Agents and Tools · Part 15 of 26
Slide: The data-plane role checklist
Run: python 03_the_data_plane_role_checklist.py
"""
# Data-plane roles a managed identity needs
ROLES = {
  "search query": "Search Index Data Reader",
  "search write":
    "Search Index Data Contributor",
  "blob": "Storage Blob Data Contributor",
  "key vault": "Key Vault Secrets User",
  "registry": "AcrPull",
  "cosmos": "Cosmos DB built-in Data Reader",
  "openai": "Cognitive Services OpenAI User",
}
print(ROLES["search query"])
