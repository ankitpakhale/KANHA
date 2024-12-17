from jsonschema import validate
from typing import Dict, Union
from .base import Base
from .. import SCHEMA_MAP
from utils import logger


class EvaluateAnswersResponsePayload(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Evaluate Answers Response Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["EVALUATE_ANSWERS"]["RESPONSE_SCHEMA"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of EvaluateAnswersResponsePayload
evaluate_answers_response_payload = EvaluateAnswersResponsePayload
