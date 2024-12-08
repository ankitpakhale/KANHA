from typing import Dict
import openai
from clients import Prompt
from .openai_base import OpenAIStrategy


class EvaluateAnswersStrategy(OpenAIStrategy, Prompt):
    """
    Strategy to evaluate programming answers using OpenAI API.
    """

    # flake8: noqa: F821
    def execute(
        self, client: "OpenAIBaseClient", user_code: Dict[str, str]
    ) -> Dict[str, str]:
        """
        Evaluate user-submitted answers.
        """
        system_prompt = self.get_answer_evaluation_system_prompt(user_code=user_code)
        user_prompt = self.get_answer_evaluation_user_prompt(user_code=user_code)

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
