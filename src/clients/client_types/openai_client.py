from typing import Optional, List, Dict
from clients import Base
import openai
from config import OpenAIConfig
from typeguard import typechecked
from utils import logger
import json


class OpenAI(Base):
    def __init__(self) -> None:
        # config data
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = OpenAIConfig.OPENAI_TEMPERATURE
        self.max_tokens = OpenAIConfig.OPENAI_MAX_TOKENS

    def __get_result(self, system_prompt: str, user_prompt: str) -> str:
        # call openai to result based on requested prompt
        __response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        # extract and return the results
        __result = __response["choices"][0]["message"]["content"]
        logger.info("Received result from OpenAI Client")
        return __result

    @typechecked
    def generate_questions(
        self,
        difficulty_level: str,
        programming_language: str,
        topics: list,
        num_questions: Optional[
            int
        ] = 20,  # adjust this value to specify the desired number of questions
    ) -> str:
        """
        Core logic to generate questions from OpenAI client
        """
        logger.info("generate_questions core logic working for OpenAI client")

        __system_prompt = self.get_question_generation_system_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=", ".join(topics),
            num_questions=num_questions,
        )
        __user_prompt = self.get_question_generation_user_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=", ".join(topics),
            num_questions=num_questions,
        )
        __generation = self.__get_result(
            system_prompt=__system_prompt, user_prompt=__user_prompt
        )

        logger.info("Received generated questions from OpenAI Client")
        return __generation

    @typechecked
    def evaluate_answers(self, user_code: List[Dict[str, str]]) -> str:
        """
        Core logic to evaluate users answer using OpenAI client
        """
        logger.info("evaluate_answers core logic working for OpenAI client")

        __system_prompt = self.get_answer_evaluation_system_prompt(user_code=user_code)
        __user_prompt = self.get_answer_evaluation_user_prompt(user_code=user_code)
        __evaluation = self.__get_result(
            system_prompt=__system_prompt, user_prompt=__user_prompt
        )
        logger.info("Received evaluated answers from OpenAI Client")
        return __evaluation
