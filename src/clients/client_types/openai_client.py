from typing import Optional, List, Dict
from clients import Base
import openai
from config import OpenAIConfig
from typeguard import typechecked


class OpenAI(Base):
    def __init__(self) -> None:
        # config data
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = OpenAIConfig.OPENAI_TEMPERATURE
        self.max_tokens = OpenAIConfig.OPENAI_MAX_TOKENS

    @typechecked
    def generate_questions(
        self,
        difficulty_level: str,
        programming_language: str,
        topics: list,
        num_questions: Optional[int] = 20,
    ):
        """
        Core logic to generate questions from OpenAI client
        """
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

        __response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": __system_prompt},
                {"role": "user", "content": __user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        # extract and return the generated questions
        __generation = __response["choices"][0]["message"]["content"]
        # logger.info(f"Received generated response from OpenAI API: {evaluation}")
        return __generation

    @typechecked
    def evaluate_answers(self, user_code: List[Dict[str, str]]):
        """
        Core logic to evaluate users answer using OpenAI client
        """
        __system_prompt = self.get_answer_evaluation_system_prompt(user_code=user_code)
        __user_prompt = self.get_answer_evaluation_user_prompt(user_code=user_code)

        __response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": __system_prompt},
                {"role": "user", "content": __user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        # extract and return the evaluation results
        __evaluation = __response["choices"][0]["message"]["content"]
        # logger.info(f"Received evaluation response from OpenAI API: {evaluation}")
        return __evaluation
