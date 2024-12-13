from clients import Client
from services import validation_payload_manager_obj
import json


class QuestionService:
    def __generate_questions(self, **kwargs):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        validation_payload_manager_obj(**kwargs)

        __client_response = Client().generate_questions(**kwargs)

        # remove escape sequences and parse JSON
        formatted_json = json.loads(__client_response)

        return formatted_json

    def generate_questions(self, **kwargs):
        return self.__generate_questions(**kwargs)


def question_service_obj(**kwargs):
    question_service_result = QuestionService().generate_questions(**kwargs)
    return question_service_result
