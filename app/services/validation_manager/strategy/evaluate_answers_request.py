from jsonschema import validate
from typing import Dict, Union
from app.services.validation_manager.strategy.base import Base
from app.utils import logger
from app.services.validation_manager.schema_map import SCHEMA_MAP


class EvaluateAnswersRequest(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Evaluate Answers Request Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["EVALUATE_ANSWERS"]["REQUEST"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of EvaluateAnswersRequest
evaluate_answers_request = EvaluateAnswersRequest
