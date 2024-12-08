from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
import openai
import json
from config import OpenAIConfig
from utils import __logger
from prompts import prompt_factory

QUESTION_GENERATION = "question_generation"
ANSWER_EVALUATION = "answer_evaluation"


class OpenAIStrategy(ABC):
    """
    Abstract base class for OpenAI strategies
    """

    @abstractmethod
    def execute(self, client: "OpenAIClient", **kwargs: Any) -> Any:
        """
        Execute the strategy logic.
        Args:
            client (OpenAIClient): The OpenAI client instance.
            kwargs: Additional arguments needed by the strategy.
        Return:
            Any: The result of the strategy execution.
        """
        raise NotImplementedError("Subclasses must implement the `execute` method.")


class OpenAIClient:
    """
    A client to interact with the OpenAI API using strategies for different operations.
    """

    def __init__(self, strategy: OpenAIStrategy) -> None:
        """
        Initialize OpenAI client with a specific strategy.
        Args:
            strategy (OpenAIStrategy): An instance of a class that implements the OpenAIStrategy interface.
        """
        print(">>>>>>>>>>>>>>>>>>> OpenAIClient is Ready!!!")
        self.strategy = strategy
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = float(OpenAIConfig.OPENAI_TEMPERATURE)
        self.max_tokens = int(OpenAIConfig.OPENAI_MAX_TOKENS)
        openai.api_key = OpenAIConfig.OPENAI_API_KEY

    def execute(self, **kwargs: Any) -> Any:
        """
        Execute the selected strategy with the provided arguments.

        Args:
            kwargs: Arguments required by the strategy.

        Returns:
            Any: The result of the strategy execution.
        """
        try:
            # self.logger.info(f"Executing strategy: {self.strategy.__class__.__name__} with arguments: {kwargs}")
            print(
                f"Executing strategy: {self.strategy.__class__.__name__} with arguments: {kwargs}"
            )
            content = self.strategy.execute(self, **kwargs)
            print("➡ ;;;;;;;;;;;;;;;;;;;;;;;;;; content:", content)

            # try to parse the response into JSON
            parsed_response = json.loads(content)

            # ensure it's an array of question objects
            if not isinstance(parsed_response, list):
                raise ValueError("The response is not a valid list of questions.")

            for question in parsed_response:
                if "q_type" not in question or "question" not in question:
                    raise ValueError(
                        "Missing required fields in one or more questions."
                    )

            return parsed_response

        except Exception as e:
            # self.logger.error(f"OpenAIClient encountered an error: {e}")
            print(f"OpenAIClient encountered an error: {e}")
            raise RuntimeError(f"OpenAI API error: {e}")


class Prompt:
    # FIXME: encapsulate all 4 methods, make them private
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
    def get_answer_evaluation_system_prompt(user_code: Dict[str, str]):
        answer_evaluation_system_prompt = prompt_factory.create_prompt(
            prompt_type=ANSWER_EVALUATION,
            user_code=user_code,
        ).get_system_prompt()
        return answer_evaluation_system_prompt

    @staticmethod
    def get_answer_evaluation_user_prompt(user_code: Dict[str, str]):
        answer_evaluation_user_prompt = prompt_factory.create_prompt(
            prompt_type=ANSWER_EVALUATION,
            user_code=user_code,
        ).get_user_prompt()
        return answer_evaluation_user_prompt


class GenerateQuestionsStrategy(OpenAIStrategy, Prompt):
    """
    Strategy to generate programming questions using OpenAI API.
    """

    def execute(
        self,
        client: OpenAIClient,
        difficulty_level: str,
        programming_language: str,
        topics: List[str],
        num_questions: Optional[int] = 20,
    ) -> List[Dict[str, str]]:
        """
        Generate Programming Questions.
        """
        system_prompt = self.get_question_generation_system_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        )
        user_prompt = self.get_question_generation_user_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        )

        # call OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model=client.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=client.temperature,
            max_tokens=client.max_tokens,
        )

        # return parsed and cleaned response
        return response.choices[0].message["content"].strip()


class EvaluateAnswersStrategy(OpenAIStrategy, Prompt):
    """
    Strategy to evaluate programming answers using OpenAI API.
    """

    def execute(
        self, client: OpenAIClient, user_code: Dict[str, str]
    ) -> Dict[str, str]:
        """
        Evaluate user-submitted answers.
        """
        system_prompt = self.get_answer_evaluation_system_prompt(user_code=user_code)
        user_prompt = self.get_answer_evaluation_user_prompt(user_code=user_code)

        # __logger.info(f"Sending prompt to OpenAI API: {user_prompt}")

        # call OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model=client.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=client.temperature,
            max_tokens=client.max_tokens,
        )

        # extract and return the evaluation results
        evaluation = response["choices"][0]["message"]["content"]
        # __logger.info(f"Received evaluation response from OpenAI API: {evaluation}")
        print(f"Received evaluation response from OpenAI API: {evaluation}")
        return evaluation


question_generation_client = OpenAIClient(GenerateQuestionsStrategy())
answer_evaluation_client = OpenAIClient(EvaluateAnswersStrategy())
