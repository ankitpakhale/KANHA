from clients import Client
from services import validation_payload_manager_obj


class EvaluationService:
    def __evaluate_answers(self, **kwargs):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        # validation_payload_manager_obj(**kwargs)

        # return the client class
        return Client().evaluate_answers(**kwargs)

    def evaluate_answers(self, **kwargs):
        return self.__evaluate_answers(**kwargs)


def evaluation_service_obj(**kwargs):
    evaluation_service_result = EvaluationService().evaluate_answers(**kwargs)
    return evaluation_service_result
