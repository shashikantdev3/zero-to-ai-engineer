"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: Add a deletion detection policy
Run: python 03_add_a_deletion_detection_policy.py
"""
# --- repeated from 02_a_change_detection_policy.py so this file runs on its own ---
P = "#Microsoft.Azure.Search."
HWM = P + "HighWaterMarkChangeDetectionPolicy"
change = {
    "@odata.type": HWM,
    "highWaterMarkColumnName": "LastModified",
}
datasource = {
    "name": "policies-ds",
    "type": "azuresql",
    "container": {"name": "dbo.PolicyDocs"},
    "dataChangeDetectionPolicy": change,
}

# --- this slide ---
SOFT = (P + "SoftDeleteColumn"
        + "DeletionDetectionPolicy")
deletion = {
    "@odata.type": SOFT,
    "softDeleteColumnName": "IsDeleted",
    "softDeleteMarkerValue": "true",
}
key = "dataDeletionDetectionPolicy"
datasource[key] = deletion
print(sorted(datasource))
