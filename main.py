import sys
from ai_reviewer.langchain_reviewer import LangChainReviewer

def main():
    diff = sys.stdin.read()
    reviewer = LangChainReviewer()
    review = reviewer.review(diff)
    print(review)

if __name__ == "__main__":
    main()