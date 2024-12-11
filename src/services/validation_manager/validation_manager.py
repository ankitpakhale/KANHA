from utils import __logger


class ValidationManager:
    """
    Validation Manager for validating payload and response
    """

    # TODO: use some design pattern to validate the data based on request_type

    def __init__(self, **kwargs):
        self.user_code = kwargs.get("user_code")
        self.num_questions = kwargs.get("num_questions")
        self.difficulty_level = kwargs.get("difficulty_level")
        self.programming_language = kwargs.get("programming_language")
        self.topics = kwargs.get("topics")
        # __logger.info(">>>>>>>>>>>>>>>>>>> Validation Manager Initialized")
        print(">>>>>>>>>>>>>>>>>>> Validation Manager Initialized")

    def __validate_types(self):
        """
        Validates the datatype of the payloads
        """
        if self.num_questions:
            assert isinstance(
                self.num_questions, int
            ), f"num_questions is not integer: {self.num_questions}"

        if self.user_code:
            assert isinstance(
                self.user_code, dict
            ), f"user_code is not dictionary: {self.user_code}"

        assert isinstance(
            self.difficulty_level, str
        ), f"difficulty_level is not string: {self.difficulty_level}"

        assert isinstance(
            self.programming_language, str
        ), f"programming_language is not string: {self.programming_language}"

        assert isinstance(self.topics, list), f"topics is not list: {self.topics}"

    def __validate_required(self):
        """
        Validates the required payloads
        """
        assert self.difficulty_level, "Difficulty level is required."

        assert self.difficulty_level in [
            "easy",
            "medium",
            "hard",
        ], "Invalid difficulty level. Choose from 'easy', 'medium', or 'hard'."

        assert self.programming_language, "Programming language is required."

        assert self.topics, "Topics are required."

    def validate_payload(self):
        """
        Validates the payload
        """
        # validates the type of the payload
        self.__validate_required()

        # validates the type of the payload
        self.__validate_types()

        print(">>>>>>>>>>>>>>>>>>> Validation Passed successfully!!!")

        return True

    def validate_response(response):
        """
        Validates the response coming from question generator
        """
        # TODO: Do this after initial version release
        ...


def validation_payload_manager_obj(**kwargs):
    validation_manager_result = ValidationManager(**kwargs).validate_payload()
    return validation_manager_result


def validation_response_manager_obj(response: dict): ...
