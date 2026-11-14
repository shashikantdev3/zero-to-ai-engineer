"""Zero to AI Engineer · RAG and Vector Search · Part 4 of 26
Slide: A prefilter in Azure AI Search
Run: python 02_a_prefilter_in_azure_ai_search.py
"""
import json
body = {
    "vectorQueries": [{
        "kind": "vector",
        "vector": [0.01, 0.02],
        "fields": "contentVector",
        "k": 10,
    }],
    "filter": "department eq 'hr'",
    "vectorFilterMode": "preFilter",
}
print(json.dumps(body, indent=2))
