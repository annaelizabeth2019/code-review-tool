from .base import AIReviewer

class LangChainReviewer(AIReviewer):
    def review(self, diff: str) -> str:
        return "AI Feedback"