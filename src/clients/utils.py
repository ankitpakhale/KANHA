from typing import Dict, Optional, List
from src.utils import logger
from prompts import prompt_factory

QUESTION_GENERATION = "question_generation"
ANSWER_EVALUATION = "answer_evaluation"


class Prompt:
    @staticmethod
    def get_question_generation_system_prompt(
        difficulty_level: str,
        programming_language: str,
        topics: str,
        num_questions: Optional[int] = 20,
    ):
        question_generation_system_prompt = prompt_factory.create_prompt(
            prompt_type=QUESTION_GENERATION,
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        ).get_system_prompt()
        return question_generation_system_prompt

    @staticmethod
    def get_question_generation_user_prompt(
        difficulty_level: str,
        programming_language: str,
        topics: str,
        num_questions: Optional[str] = 20,
    ):
        question_generation_user_prompt = prompt_factory.create_prompt(
            prompt_type=QUESTION_GENERATION,
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        ).get_user_prompt()
        return question_generation_user_prompt

    @staticmethod
    def get_answer_evaluation_system_prompt(user_code: List[Dict[str, str]]):
        answer_evaluation_system_prompt = prompt_factory.create_prompt(
            prompt_type=ANSWER_EVALUATION,
            user_code=user_code,
        ).get_system_prompt()
        return answer_evaluation_system_prompt

    @staticmethod
    def get_answer_evaluation_user_prompt(user_code: List[Dict[str, str]]):
        answer_evaluation_user_prompt = prompt_factory.create_prompt(
            prompt_type=ANSWER_EVALUATION,
            user_code=user_code,
        ).get_user_prompt()
        return answer_evaluation_user_prompt
