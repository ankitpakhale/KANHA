from typing import Union, Dict, List
from app.clients import Client
from app.services import validation_manager
import json
from app.utils import logger
from app.control_panel import control_panel_manager

# TODO: change name to EvaluateAnswers


class EvaluationService:
    @staticmethod
    def __validate_request_data(payload: Dict[str, Union[str, List[str]]]) -> None:
        # whole payload is getting validated at once
        validation_manager(
            service_type="evaluate_answers", validation_type="request"
        ).validate(payload)

    def __evaluate_answers(self, payload: Union[list, dict]):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        self.__validate_request_data(payload)
        logger.debug("User request data validated at question service")

        # return the client class
        __client_response = Client().evaluate_answers(payload)

        # remove escape sequences and parse JSON
        formatted_json = json.loads(__client_response)

        # TODO: add response validation layer

        return formatted_json

    def evaluate_answers(self, payload: Union[list, dict]):
        if control_panel_manager.get_setting("EVALUATE_ANSWERS_FROM_CLIENT"):
            data = self.__evaluate_answers(payload)
        else:
            logger.warning(
                """
                The 'EVALUATE_ANSWERS_FROM_CLIENT' setting is currently disabled in the control panel.
                If this setting was not intentionally turned off, please enable it to allow evaluating
                answers dynamically based on the client request.

                WARNING: The fallback to static data from the 'evaluate_answers.json' file is only for testing purposes.
                Do not use this approach in production environments, as it bypasses dynamic answer evaluation
                and relies on hardcoded data. Ensure that the setting is enabled in production to maintain correct
                functionality and avoid potential issues.
                """
            )
            # path of JSON file
            json_file_path = "app/payloads/response_examples/evaluate_answers.json"

            # open and read the JSON file
            with open(json_file_path, "r") as file:
                data = json.load(file)

        return data


evaluation_service = EvaluationService
# def evaluation_service_obj(payload: Union[list, dict]):
#     evaluation_service_result = EvaluationService().evaluate_answers(payload)
#     return evaluation_service_result
