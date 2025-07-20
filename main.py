import os
import json

def main():
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        print("GITHUB_EVENT_PATH is not set.")
        return

    with open(event_path, 'r') as f:
        event_data = json.load(f)

    # Safely access PR fields
    pr_data = event_data.get("pull_request")
    if not pr_data:
        print("No 'pull_request' data found in the event payload.")
        return

    title = pr_data.get("title", "N/A")
    number = pr_data.get("number", "N/A")
    html_url = pr_data.get("html_url", "N/A")
    diff_url = pr_data.get("diff_url", "N/A")
    base_branch = pr_data.get("base", {}).get("ref", "N/A")
    head_branch = pr_data.get("head", {}).get("ref", "N/A")

    print(f"🔍 PR #{number}: {title}")
    print(f"📎 URL: {html_url}")
    print(f"📄 Diff URL: {diff_url}")
    print(f"🌿 {head_branch} → {base_branch}")

    # You can now fetch the diff, analyze changed files, etc.

if __name__ == "__main__":
    main()
