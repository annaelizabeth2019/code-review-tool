import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_diff_with_openai(diff: str) -> str:
    prompt = (
        "You are a senior software engineer reviewing a GitHub pull request. "
        "Your task is to analyze the code changes and write a review comment in GitHub-flavored markdown. "
        "Structure the output with **headings**, **bullet points**, and use ``````` for code blocks if relevant.\n\n"
        "Start your comment like this:\n\n"
        "**🤖 AI Review Summary**\n\n"
        "Then include findings such as:\n\n"
        "- ✅ Improvements\n"
        "- ⚠️ Suggestions\n"
        "- ❌ Issues\n\n"
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
