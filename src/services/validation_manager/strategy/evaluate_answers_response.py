from jsonschema import validate
from typing import Dict, Union
from .base import Base
from utils import logger
from services.validation_manager.constants import SCHEMA_MAP


class EvaluateAnswersResponse(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Evaluate Answers Response Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["EVALUATE_ANSWERS"]["RESPONSE_SCHEMA"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of EvaluateAnswersResponse
evaluate_answers_response = EvaluateAnswersResponse
