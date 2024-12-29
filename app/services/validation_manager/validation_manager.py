from typing import Union
from app.services.validation_manager.strategy import (
    generate_questions_request,
    generate_questions_response,
    evaluate_answers_request,
    evaluate_answers_response,
    feedback_request,
)

# from app.utils import logger
STRATEGY_MAP = {
    "generate_questions_request": generate_questions_request,
    "generate_questions_response": generate_questions_response,
    "evaluate_answers_request": evaluate_answers_request,
    "evaluate_answers_response": evaluate_answers_response,
    "feedback_request": feedback_request,
}


class ValidationManager:
    def __init__(self, service_type: str, validation_type: str) -> None:
        # service_type = generate_questions or evaluate_answers
        # validation_type = request or response
        __type = f"{service_type}_{validation_type}"
        self.strategy = STRATEGY_MAP.get(__type)()
        if not self.strategy:
            __msg = f"Invalid {__type} strategy while validation"
            # logger.error(__msg)
            raise ValueError(__msg)
        # logger.debug(f"{__type} strategy assigned while validation")

    def validate(self, payload: Union[list, dict]) -> bool:
        return self.strategy.validate(payload=payload)


# singleton instance of ValidationManager
validation_manager_obj = ValidationManager
