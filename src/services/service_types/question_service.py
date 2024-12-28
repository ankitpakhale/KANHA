from typing import Union, List, Dict
from clients import Client
from services import validation_manager_obj
import json
from utils import logger
from uuid import uuid4


# TODO: change name to GenerateQuestions
class QuestionService:
    @staticmethod
    def __add_id_in_response(response: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Add q_id in all the questions based on question type.
        """
        __response = list(
            map(
                lambda res: {
                    **res,
                    "q_id": (
                        f"mcq{''.join(str(uuid4()).replace('-', ''))}"
                        if "options" in res
                        else f"psq{''.join(str(uuid4()).replace('-', ''))}"
                    ),
                },
                response,
            )
        )
        return __response

    def __generate_questions(
        self, payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        __validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="request"
        )
        __validation_manager.validate(payload)
        logger.debug("Payload varified successfully at Question Service!!!")

        __client_response = Client().generate_questions(payload)
        logger.info(f"Received Questions from Client: {__client_response}")

        # remove escape sequences and parse JSON
        __formatted_json = json.loads(__client_response)

        # add q_id in all the questions
        __formatted_json_with_id = self.__add_id_in_response(__formatted_json)
        return __formatted_json_with_id

    def generate_questions(
        self, payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        return self.__generate_questions(payload)


def question_service_obj(
    payload: Dict[str, Union[str, List[str]]]
) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
    question_service_result = QuestionService().generate_questions(payload)
    return question_service_result
