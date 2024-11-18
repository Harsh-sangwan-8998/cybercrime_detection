import json
import os

def collect_evidence(data):
    evidence_path = "evidence.json"
    
    # Load existing evidence data, handling JSON decoding errors
    if os.path.exists(evidence_path):
        try:
            with open(evidence_path, "r") as f:
                evidence = json.load(f)
        except json.JSONDecodeError:
            print("Warning: evidence.json file is corrupted or invalid. Starting with an empty list.")
            evidence = []
    else:
        evidence = []

    evidence.append(data)

    with open(evidence_path, "w") as f:
        json.dump(evidence, f, indent=4)

    print(f"Evidence collected: {data}")
    return data