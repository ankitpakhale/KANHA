from abc import ABC, abstractmethod
from .utils import Prompt


class BaseClient(ABC, Prompt):
    @abstractmethod
    def generate_questions():
        pass

    @abstractmethod
    def evaluate_answers():
        pass
