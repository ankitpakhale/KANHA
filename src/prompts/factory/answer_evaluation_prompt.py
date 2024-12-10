from prompts import ANSWER_EVALUATION_SYSTEM_PROMPT, ANSWER_EVALUATION_USER_PROMPT
from .base_prompt import BasePrompt
from typing import Dict, List


class AnswerEvaluationPrompt(BasePrompt):
    """
    Class to handle answer evaluation prompts.
    """

    def __init__(self, user_code: Dict):
        self.user_code = user_code

    @staticmethod
    def get_system_prompt():
        """
        Returns the system prompt for answer evaluation
        """
        return ANSWER_EVALUATION_SYSTEM_PROMPT

    def get_user_prompt(self):
        """
        Returns the user prompt for answer evaluation
        """
        return ANSWER_EVALUATION_USER_PROMPT.format(code=self.user_code)
