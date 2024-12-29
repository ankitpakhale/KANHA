from .question_generation_prompt import QuestionGenerationPrompt
from .answer_evaluation_prompt import AnswerEvaluationPrompt


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


prompt_factory = PromptFactory()
