import json

def triage(text: str) -> dict:
    text_l = text.lower()
    if "fraud" in text_l or "hacked" in text_l:
        urgency = "critical"
        escalate = True
    elif "failed" in text_l or "debited" in text_l:
        urgency = "high"
        escalate = True
    elif "slow" in text_l or "delay" in text_l:
        urgency = "medium"
        escalate = False
    else:
        urgency = "low"
        escalate = False

    return {
        "complaint": text,
        "urgency": urgency,
        "escalate": escalate,
    }

cases = [
    "My transfer failed, money was debited",
    "App is slow today",
    "I think my account was hacked",
]

results = [triage(c) for c in cases]

print(json.dumps(results, indent=2))

with open("triage_output.json", "w") as f:
    json.dump(results, f, indent=2)

print("Wrote triage_output.json")