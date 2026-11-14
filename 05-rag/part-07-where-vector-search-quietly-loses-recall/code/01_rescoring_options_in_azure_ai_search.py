"""Zero to AI Engineer · RAG and Vector Search · Part 7 of 26
Slide: Rescoring Options in Azure AI Search
Run: python 01_rescoring_options_in_azure_ai_search.py
"""
# Azure AI Search compression config
# (illustrative; check names per API version)
store = "preserveOriginals"
compressions = [{
    "name": "sq-int8",
    "kind": "scalarQuantization",
    "rescoringOptions": {
        "enableRescoring": True,
        "defaultOversampling": 4,
        "rescoreStorageMethod": store,
    },
}]
