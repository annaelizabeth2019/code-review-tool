import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_diff_with_openai(diff: str) -> str:
    prompt = (
        "You are a senior software engineer reviewing a GitHub pull request. "
        "Your job is to analyze the provided diff and give concise, specific, constructive, and helpful feedback in GitHub-flavored Markdown (GFM).\n\n"
        "Please format your response using clear headings, bullet points, and code blocks where appropriate.\n\n"
        "Structure your response as follows:\n\n"
        "**## 🤖 AI Review Summary**\n\n"
        "- A high-level summary of what the changes do.\n\n"
        "**## ✅ Praise**\n"
        "- Note any well-written, efficient, or thoughtful code.\n\n"
        "**## ⚠️ Suggestions**\n"
        "- Suggest improvements, refactoring, or better practices.\n\n"
        "**## ❌ Potential Issues**\n"
        "- Flag any bugs, security concerns, or major design problems.\n\n"
        "Use GitHub Markdown features like `###`, `-`, and ````` where appropriate.\n\n"
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
