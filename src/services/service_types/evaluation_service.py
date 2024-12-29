from typing import Union
from src.clients import Client
from src.services import validation_manager_obj
import json
from src.utils import logger

# TODO: change name to EvaluateAnswers


class EvaluationService:
    def __evaluate_answers(self, payload: Union[list, dict]):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        validation_manager = validation_manager_obj(
            service_type="evaluate_answers", validation_type="request"
        )
        validation_manager.validate(payload)
        logger.debug("Payload varified successfully at Evaluation Service!!!")

        # return the client class
        __client_response = Client().evaluate_answers(payload)

        # remove escape sequences and parse JSON
        formatted_json = json.loads(__client_response)

        return formatted_json

    def evaluate_answers(self, payload: Union[list, dict]):
        return self.__evaluate_answers(payload)


def evaluation_service_obj(payload: Union[list, dict]):
    evaluation_service_result = EvaluationService().evaluate_answers(payload)
    return evaluation_service_result
