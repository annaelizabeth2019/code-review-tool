import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_diff_with_openai(diff: str) -> str:
    prompt = (
        "You are a senior software engineer reviewing a pull request. "
        "Suggest improvements, point out issues, and praise good practices. "
        "Summarize the changes in a concise manner.\n\n"
        f"Here is the PR diff:\n\n{diff}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a thoughtful and constructive PR reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
