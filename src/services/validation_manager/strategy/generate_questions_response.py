from jsonschema import validate
from typing import Dict, Union
from .base import Base
from utils import logger
from services.validation_manager.schema_map import SCHEMA_MAP


class GenerateQuestionsResponse(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Generate Questions Response Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        schema = SCHEMA_MAP["GENERATE_QUESTIONS"]["RESPONSE"]
        return self.__validate(payload=payload, schema=schema)


# singleton instance of GenerateQuestionsResponse
generate_questions_response = GenerateQuestionsResponse
