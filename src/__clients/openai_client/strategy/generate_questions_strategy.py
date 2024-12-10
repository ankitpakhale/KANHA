from typing import List, Dict, Optional
import openai
from clients import Prompt
from ..base import OpenAIBaseStrategy


class GenerateQuestionsStrategy(OpenAIBaseStrategy, Prompt):
    """
    Strategy to generate programming questions using OpenAI API.
    """

    # flake8: noqa: F821
    def execute(
        self,
        client: "OpenAIBaseClient",
        difficulty_level: str,
        programming_language: str,
        topics: List[str],
        num_questions: Optional[int] = 20,
    ) -> List[Dict[str, str]]:
        """
        Generate programming questions.
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

        response = openai.ChatCompletion.create(
            model=client.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=client.temperature,
            max_tokens=client.max_tokens,
        )

        # extract and return the generated questions
        generation = response["choices"][0]["message"]["content"]
        # __logger.info(f"Received generated response from OpenAI API: {evaluation}")
        print(f"Received generated response from OpenAI API: {generation}")
        return generation
