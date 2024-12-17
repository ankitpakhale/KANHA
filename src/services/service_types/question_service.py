from clients import Client
from services import validation_manager_obj
import json

# TODO: change name to GenerateQuestions


class QuestionService:
    def __generate_questions(self, **kwargs):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="request"
        )
        validation_status = validation_manager.validate(**kwargs)
        print("➡ &&&&&&&&&&&&&&&&&&&&&&&&&&&9 validation_status:", validation_status)

        __client_response = Client().generate_questions(**kwargs)

        # remove escape sequences and parse JSON
        formatted_json = json.loads(__client_response)

        return formatted_json

    def generate_questions(self, **kwargs):
        return self.__generate_questions(**kwargs)


def question_service_obj(**kwargs):
    question_service_result = QuestionService().generate_questions(**kwargs)
    return question_service_result
