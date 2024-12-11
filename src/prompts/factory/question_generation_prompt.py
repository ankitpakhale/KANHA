from typing import Optional
from prompts import QUESTION_GENERATION_SYSTEM_PROMPT, QUESTION_GENERATION_USER_PROMPT
from .base_prompt import BasePrompt


class QuestionGenerationPrompt(BasePrompt):
    """
    Class to handle question generation prompts.
    """

    # TODO: remove this init and directly pass these data in specific method using **kwargs
    def __init__(
        self,
        difficulty_level: str,
        programming_language: str,
        topics: list,
        num_questions: Optional[str] = 20,
    ):
        self.num_questions = num_questions
        self.difficulty_level = difficulty_level
        self.programming_language = programming_language
        self.topics = topics

    @staticmethod
    def get_system_prompt():
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
