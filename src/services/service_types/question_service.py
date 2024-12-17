from typing import Union
from clients import Client
from services import validation_manager_obj
import json
from utils import logger

# TODO: change name to GenerateQuestions


class QuestionService:
    def __generate_questions(self, payload: Union[list, dict]):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="request"
        )
        validation_manager.validate(payload)
        logger.debug("Payload varified successfully at Question Service!!!")

        __client_response = Client().generate_questions(payload)

        # remove escape sequences and parse JSON
        formatted_json = json.loads(__client_response)

        return formatted_json

    def generate_questions(self, payload: Union[list, dict]):
        return self.__generate_questions(payload)


def question_service_obj(payload: Union[list, dict]):
    question_service_result = QuestionService().generate_questions(payload)
    return question_service_result
