from jsonschema import validate
from typing import Dict, Union
from .base import Base
from utils import logger
from services.validation_manager.schema_map import SCHEMA_MAP


class GenerateQuestionsRequest(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Generate Questions Request Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["GENERATE_QUESTIONS"]["REQUEST"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of GenerateQuestionsRequest
generate_questions_request = GenerateQuestionsRequest
