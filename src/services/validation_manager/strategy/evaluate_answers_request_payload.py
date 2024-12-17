from jsonschema import validate
from typing import Dict, Union
from .base import Base
from .. import SCHEMA_MAP
from utils import logger


class EvaluateAnswersRequestPayload(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Evaluate Answers Request Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["EVALUATE_ANSWERS"]["REQUEST_SCHEMA"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of EvaluateAnswersRequestPayload
evaluate_answers_request_payload = EvaluateAnswersRequestPayload
