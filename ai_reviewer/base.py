from abc import ABC, abstractmethod

class AIReviewer(ABC):
    @abstractmethod
    def review(self, diff: str) -> str:
        pass