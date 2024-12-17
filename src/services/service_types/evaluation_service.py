from clients import Client
from services import validation_manager_obj
import json

# TODO: change name to EvaluateAnswers


class EvaluationService:
    def __evaluate_answers(self, **kwargs):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        validation_manager_obj(
            service_type="evaluate_answers", validation_type="request"
        ).validate(**kwargs)

        # return the client class
        __client_response = Client().evaluate_answers(**kwargs)

        # remove escape sequences and parse JSON
        formatted_json = json.loads(__client_response)

        return formatted_json

    def evaluate_answers(self, **kwargs):
        return self.__evaluate_answers(**kwargs)


def evaluation_service_obj(**kwargs):
    evaluation_service_result = EvaluationService().evaluate_answers(**kwargs)
    return evaluation_service_result
