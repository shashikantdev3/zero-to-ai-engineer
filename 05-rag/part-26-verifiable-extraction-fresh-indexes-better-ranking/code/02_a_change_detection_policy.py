"""Zero to AI Engineer · RAG and Vector Search · Part 26 of 26
Slide: A change detection policy
Run: python 02_a_change_detection_policy.py
"""
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
