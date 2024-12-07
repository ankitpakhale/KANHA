from typing import Optional
from abc import ABC, abstractmethod
from answer_evaluation import (
    ANSWER_EVALUATION_SYSTEM_PROMPT,
    ANSWER_EVALUATION_USER_PROMPT,
)
from question_generation import (
    QUESTION_GENERATION_SYSTEM_PROMPT,
    QUESTION_GENERATION_USER_PROMPT,
)


class PromptFactory:
    """
    The factory class responsible for creating prompts based on the given type and parameters.
    """

    @staticmethod
    def create_prompt(prompt_type: str, **kwargs):
        """
        Factory method to create the appropriate prompt instance based on the prompt type.
        """
        if prompt_type == "question_generation":
            return QuestionGenerationPrompt(**kwargs)
        elif prompt_type == "answer_evaluation":
            return AnswerEvaluationPrompt(**kwargs)
        else:
            raise ValueError(f"Unknown prompt type: {prompt_type}")


class QuestionGenerationPrompt:
    """
    Class to handle question generation prompts.
    """

    def __init__(
        self,
        difficulty_level: str,
        programming_language: str,
        topics: str,
        num_questions: Optional[str] = 20,
    ):
        self.num_questions = num_questions
        self.difficulty_level = difficulty_level
        self.programming_language = programming_language
        self.topics = topics

    def get_system_prompt(self):
        """
        Returns the system prompt for question generation
        """
        return QUESTION_GENERATION_SYSTEM_PROMPT

    def get_user_prompt(self):
        """
        Returns the user prompt for question generation
        """
        return QUESTION_GENERATION_USER_PROMPT.format(
            num_questions=self.num_questions,
            difficulty_level=self.difficulty_level,
            programming_language=self.programming_language,
            topics=self.topics,
        )


class AnswerEvaluationPrompt:
    """
    Class to handle answer evaluation prompts.
    """

    def __init__(self, user_code: str):
        self.user_code = user_code

    def get_system_prompt(self):
        """
        Returns the system prompt for answer evaluation
        """
        return ANSWER_EVALUATION_SYSTEM_PROMPT.format(code=self.user_code)

    def get_user_prompt(self):
        """
        Returns the user prompt for answer evaluation
        """
        return ANSWER_EVALUATION_USER_PROMPT.format(code=self.user_code)


prompt_factory = PromptFactory()
