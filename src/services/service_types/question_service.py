from clients import Client
from services import validation_payload_manager_obj


class QuestionService:
    def __generate_questions(self, **kwargs):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        validation_payload_manager_obj(**kwargs)

        # return the client class
        return Client().generate_questions(**kwargs)

    def generate_questions(self, **kwargs):
        return self.__generate_questions(**kwargs)


def question_service_obj(**kwargs):
    question_service_result = QuestionService().generate_questions(**kwargs)
    return question_service_result
