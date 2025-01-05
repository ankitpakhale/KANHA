from jsonschema import validate
from typing import Dict, Union
from app.services.validation_manager.strategy.base import Base
from app.utils import logger
from app.services.validation_manager.schema_map import SCHEMA_MAP


class EvaluateAnswersResponse(Base):
    @staticmethod
    def __validate(payload: Union[list, dict], schema: Dict):
        validate(instance=payload, schema=schema)
        logger.debug("Evaluate Answers Response Payload validated successfully!!!")
        return True

    def validate(self, payload: Union[list, dict]) -> bool:
        if self.control_panel_manager.get_setting("VALIDATE_RESPONSE_DATA"):
            schema = SCHEMA_MAP["EVALUATE_ANSWERS"][""]
            status = self.__validate(payload=payload, schema=schema)
        else:
            logger.warning(
                """
                Response data validation is currently disabled (VALIDATE_RESPONSE_DATA setting is False in the control panel).
                As a result, the outgoing payload will not be validated against the expected schema.
                This may lead to unexpected behavior or issues if the data structure is incorrect.
                """
            )
            status = True
        return status


# singleton instance of EvaluateAnswersResponse
evaluate_answers_response = EvaluateAnswersResponse
