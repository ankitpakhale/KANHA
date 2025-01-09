from typing import Union, List, Dict
from uuid import uuid4
import json
from app.clients import Client
from app.services import validation_manager_obj
from app.utils import logger
from app.dao import (
    MultipleChoiceQuestion,
    ProblemSolvingQuestion,
    db_session,
)
from app.control_panel import control_panel_manager


# TODO: change name to GenerateQuestions
class QuestionService:
    @staticmethod
    def __validate_request_data(payload: Dict[str, Union[str, List[str]]]) -> None:
        __validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="request"
        )
        __validation_manager.validate(payload)

    @staticmethod
    def __get_data_from_client(
        payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        if control_panel_manager.get_setting("GENERATE_QUESTIONS_FROM_CLIENT"):
            __client_response = Client().generate_questions(payload)
            logger.debug("Client data received at question service")
        else:
            logger.warning(
                """
                The 'GENERATE_QUESTIONS_FROM_CLIENT' setting is currently disabled in the control panel.
                If this setting was not intentionally turned off, please enable it to allow generating
                questions dynamically from the client request.

                WARNING: This fallback to static data from the 'generate_questions.json' file is only for testing purposes.
                Do not rely on this setting in production environments, as it bypasses dynamic generation
                and uses hardcoded data. Ensure the setting is enabled for production to avoid potential issues.
                """
            )
            # path of JSON file
            json_file_path = "app/payloads/response_examples/generate_questions.json"

            # open and read the JSON file
            with open(json_file_path, "r") as file:
                __client_response = json.load(file)

        logger.debug(f"Received Questions from Client: {__client_response}")
        return __client_response

    @staticmethod
    def __validate_response_data(response: List[Dict[str, str]]) -> None:
        __validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="response"
        )
        for res in response:
            __validation_manager.validate(res)

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

        logger.debug("Added IDs in validated client data at question service")
        return __response

    @staticmethod
    def __save_client_response(
        payload: Dict[str, Union[str, List[str]]], response: List[Dict[str, str]]
    ) -> None:
        if not control_panel_manager.get_setting("SAVE_CLIENT_RESPONSE_IN_DB"):
            logger.warning(
                """
            The 'SAVE_CLIENT_RESPONSE_IN_DB' setting is currently disabled in the control panel.
            If this setting was not intentionally turned off, please enable it to allow saving
            client responses in the database.

            WARNING: With this setting disabled, client responses will not be persisted in the database.
            This behavior is typically only used in testing environments. Ensure that this setting is enabled
            in production to maintain data integrity and avoid potential issues with missing responses.
            """
            )
            return

        # create the session
        session = db_session()

        # get the difficulty level from user payload
        __difficulty_level = payload["difficulty_level"]

        for selected_ques in response:
            # get the type of question based on q_id
            q_type = selected_ques["q_id"][:3]
            if q_type == "mcq":
                entry = MultipleChoiceQuestion(
                    difficulty_level=__difficulty_level,
                    question=selected_ques["problem_description"],
                    option_1=selected_ques["options"][0],
                    option_2=selected_ques["options"][1],
                    option_3=selected_ques["options"][2],
                    option_4=selected_ques["options"][3],
                    correct_answer=selected_ques["correct_answer"],
                )
                q_obj = (
                    session.query(MultipleChoiceQuestion)
                    .filter(MultipleChoiceQuestion.question == entry.question)
                    .all()
                )
            else:
                entry = ProblemSolvingQuestion(
                    difficulty_level=__difficulty_level,
                    problem_description=selected_ques["problem_description"],
                    input_format=selected_ques["input_format"],
                    output_format=selected_ques["output_format"],
                    constraints=selected_ques["constraints"],
                    examples=selected_ques["examples"],
                    edge_cases=selected_ques["edge_cases"],
                )
                q_obj = (
                    session.query(ProblemSolvingQuestion)
                    .filter(
                        ProblemSolvingQuestion.problem_description
                        == entry.problem_description
                    )
                    .all()
                )

            if not q_obj:
                session.add(entry)
                session.commit()
                logger.debug(
                    f"===> {(q_type).upper()} type question added successfully!!!"
                )
            else:
                logger.debug(f"===> This {(q_type).upper()} question is already in DB")

        logger.debug("Client data saved in DB at question service")

    def __generate_questions(self, payload: Dict[str, Union[str, List[str]]]):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        self.__validate_request_data(payload)
        logger.debug("User request data validated at question service")

        # get data from appropriate client and parse the JSON
        __client_response = self.__get_data_from_client(payload)

        # validate client response
        self.__validate_response_data(__client_response)

        # add q_id in all the questions
        __formatted_json_with_id = self.__add_id_in_response(__client_response)

        # save client response in DB
        self.__save_client_response(payload, __formatted_json_with_id)

        return __formatted_json_with_id

    def generate_questions(
        self, payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        return self.__generate_questions(payload)


# TODO: simplify this service obj method, add singleton design pattern
def question_service_obj(
    payload: Dict[str, Union[str, List[str]]]
) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
    question_service_result = QuestionService().generate_questions(payload)
    return question_service_result
