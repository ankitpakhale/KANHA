from utils.logging import __logger


class ValidationManager:
    """
    Validation Manager for validating payload and response
    """

    def __init__(self, difficulty_level: str, programming_language: str, topics: str):
        self.difficulty_level = difficulty_level
        self.programming_language = programming_language
        self.topics = topics
        print(">>>>>>>>>>>>>>>>>>> Validation Manager Initialized")

    def __validate_types(self):
        """
        Validates the datatype of the payloads
        """
        assert isinstance(
            self.difficulty_level, str
        ), f"difficulty_level is not string: {self.difficulty_level}"

        assert isinstance(
            self.programming_language, str
        ), f"programming_language is not string: {self.programming_language}"

        assert isinstance(self.topics, str), f"topics is not string: {self.topics}"

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


def validation_payload_manager_obj(
    difficulty_level: str, programming_language: str, topics: str
):
    validation_manager_result = ValidationManager(
        difficulty_level, programming_language, topics
    ).validate_payload()
    return validation_manager_result


def validation_response_manager_obj(response: dict): ...
