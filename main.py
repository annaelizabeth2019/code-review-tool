import os
import json
import requests

# Add dotenv for local development
if not os.getenv("GITHUB_ACTIONS"):  # Only load .env if not in GitHub Actions
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("python-dotenv not installed. Install it for local development.")
from ai_reviewer.openai import review_diff_with_openai


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
    diff_url = pr_data.get("diff_url", "N/A")

    print(f"📥 Fetching diff... {diff_url}")
    diff_resp = requests.get(diff_url, headers={"Accept": "application/vnd.github.v3.diff"})
    if diff_resp.status_code != 200:
        print(f"❌ Failed to fetch diff: {diff_resp.status_code}")
        return

    diff_text = diff_resp.text
    print(f"✅ Diff fetched ({len(diff_text.splitlines())} lines)")

    # Call OpenAI
    print("🧠 Sending to OpenAI...")
    ai_response = review_diff_with_openai(f"PR Title: {title}\n\n{diff_text}")

    print("💬 AI Review Response:")
    print(ai_response)

    # You can now fetch the diff, analyze changed files, etc.

if __name__ == "__main__":
    main()
