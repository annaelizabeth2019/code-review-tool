import json, os

with open(os.getenv("GITHUB_EVENT_PATH")) as f:
    event_data = json.load(f)
    print("Full event path:", event_data)
