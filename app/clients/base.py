from abc import ABC, abstractmethod
from app.clients.utils import Prompt


class Base(ABC, Prompt):
    @abstractmethod
    def generate_questions():
        pass

    @abstractmethod
    def evaluate_answers():
        pass
