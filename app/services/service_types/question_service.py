from typing import Union, List, Dict
from uuid import uuid4
import json
from app.clients import Client
from app.services import validation_manager
from app.utils import logger
from app.dao import (
    MultipleChoiceQuestion,
    ProblemSolvingQuestion,
    db_session,
)
from app.control_panel import control_panel_manager


class QuestionClient:
    @staticmethod
    def generate_questions(
        payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        if control_panel_manager.get_setting("GENERATE_QUESTIONS_FROM_CLIENT"):
            client_response = Client().generate_questions(payload)
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
                client_response = json.load(file)

        logger.debug(f"Received Questions from Client: {client_response}")
        return client_response


class QuestionFormatter:
    @staticmethod
    def add_ids(response: List[Dict[str, str]]) -> List[Dict[str, str]]:
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
                        else (
                            f"psq{''.join(str(uuid4()).replace('-', ''))}"
                            if "q_id" not in res
                            else res["q_id"]
                        )
                    ),
                },
                response,
            )
        )

        logger.debug("Added IDs in validated client data at question service")
        return __response


class QuestionValidator:
    def __init__(self, type: str, payload: dict) -> None:
        self.type = type
        self.payload = payload
        self.GENERATE_QUESTIONS = "generate_questions"
        self.__adjust_payload()

    def __adjust_payload(self) -> None:
        if self.type == "request":
            self.payload = [
                self.payload
            ]  # if the type is request add payload obj in list

    def validate(self) -> None:
        validation_manager_obj = validation_manager(
            service_type=self.GENERATE_QUESTIONS, validation_type=self.type
        )
        for res in self.payload:
            validation_manager_obj.validate(res)

        logger.debug(f"{self.type} data validated at question service")


class TimeCalculator:
    def calculate_time(
        payload: Dict[str, str], response: List[Dict[str, str]]
    ) -> List[Dict[str, str]]:
        TIME_MAP = {
            "EASY": {
                "MCQ": 1,
                "PSQ": 5,  # psq can't be in easy level, for safe side we have added this
            },
            "MEDIUM": {
                "MCQ": 2,
                "PSQ": 10,
            },
            "HARD": {
                "MCQ": 2,  # mcq can't be in hard level, for safe side we have added this
                "PSQ": 15,
            },
        }
        # get the difficulty level from user payload
        difficulty_level = payload["difficulty_level"].upper()
        __response = list(
            map(
                lambda res: {
                    **res,
                    "required_time": TIME_MAP[difficulty_level][
                        res["q_id"][:3].upper()
                    ],
                },
                response,
            )
        )
        return __response


class QuestionRepository:
    @staticmethod
    def save(
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
        difficulty_level = payload["difficulty_level"]

        for selected_ques in response:
            # get the type of question based on q_id
            q_type = selected_ques["q_id"][:3]
            if q_type == "mcq":
                entry = MultipleChoiceQuestion(
                    difficulty_level=difficulty_level,
                    question=selected_ques["problem_description"],
                    option_1=selected_ques["options"][0],
                    option_2=selected_ques["options"][1],
                    option_3=selected_ques["options"][2],
                    option_4=selected_ques["options"][3],
                    correct_answer=selected_ques["correct_answer"],
                    required_time=selected_ques["required_time"],
                )
                q_obj = (
                    session.query(MultipleChoiceQuestion)
                    .filter(MultipleChoiceQuestion.question == entry.question)
                    .all()
                )
            else:
                entry = ProblemSolvingQuestion(
                    difficulty_level=difficulty_level,
                    problem_description=selected_ques["problem_description"],
                    input_format=selected_ques["input_format"],
                    output_format=selected_ques["output_format"],
                    constraints=selected_ques["constraints"],
                    examples=selected_ques["examples"],
                    edge_cases=selected_ques["edge_cases"],
                    required_time=selected_ques["required_time"],
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


class QuestionService:
    def __generate_questions(self, payload: Dict[str, Union[str, List[str]]]):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the request data
        question_validator = QuestionValidator(type="request", payload=payload)
        question_validator.validate()

        # get data from appropriate client and parse the JSON
        client_response = QuestionClient.generate_questions(payload)

        # validate the response data
        question_validator = QuestionValidator(type="response", payload=client_response)
        question_validator.validate()

        # add q_id in all the questions
        response_with_id = QuestionFormatter.add_ids(client_response)
        response_with_required_time = TimeCalculator.calculate_time(
            payload=payload, response=response_with_id
        )
        print(f"==>> response_with_required_time: {response_with_required_time}")

        # save client response in DB
        QuestionRepository.save(payload, response_with_required_time)
        return response_with_required_time

    def generate_questions(
        self, payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        return self.__generate_questions(payload)


# singleton instance of QuestionService
question_service = QuestionService
