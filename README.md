**WIP: this project still has more features coming soon!**

**Upcoming features:**
- Improved feedback formatting
- Pass/Fail recommendation and configuration options
- Comments on PRs (currently in feature branch)

# AI PR Reviewer

Generates concise summaries and suggestions for GitHub Pull Requests using GPT-4.

## Features
- Summarizes PR changes
- Suggests improvements and points out issues
- Praises good practices

## Usage as a GitHub Action
This project is designed to run as a GitHub Action using Docker. It fetches the PR diff and sends it to OpenAI for review.

**Minimal example:**
```yaml
- name: AI PR Reviewer
  uses: annaelizabeth2019/code-review-tool@main
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## Local Development & Testing

1. **Clone the repository:**
   ```bash
   git clone https://github.com/annaelizabeth2019/code-review-tool.git
   cd code-review-tool
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     GITHUB_EVENT_PATH=sample_event.json
     ```
   - Or export them directly in your shell.

4. **Run the tool locally:**
   ```bash
   python main.py
   ```
   This will use `sample_event.json` as the event payload and print the AI review to the console.

## Configuration
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `GITHUB_EVENT_PATH`: Path to the GitHub event JSON (set automatically in Actions, set manually for local testing)

## Project Structure
- `main.py` — Entry point, handles event and diff fetching
- `ai_reviewer/openai.py` — Handles OpenAI API calls
- `sample_event.json` — Example event payload for local testing
- `action.yml` — GitHub Action definition
- `Dockerfile` — Container setup for GitHub Actions

## Contributing
Pull requests and issues are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## License
MIT
