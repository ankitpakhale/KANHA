from jsonschema import validate
from typing import Dict, Union
from src.services.validation_manager.strategy.base import Base
from src.utils import logger
from src.services.validation_manager.schema_map import SCHEMA_MAP


class EvaluateAnswersResponse(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Evaluate Answers Response Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["EVALUATE_ANSWERS"]["RESPONSE"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of EvaluateAnswersResponse
evaluate_answers_response = EvaluateAnswersResponse
