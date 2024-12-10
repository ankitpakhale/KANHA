from config import GeneralConfig
from clients import Bedrock, OpenAI


class QuestionService:
    def __init__(self, difficulty_level: str, programming_language: str, topics: dict):
        self.__difficulty_level = difficulty_level
        self.__programming_language = programming_language
        self.__topics = topics
        self.__client = (
            OpenAI if GeneralConfig.ACTIVE_CLIENT == OpenAI.__name__ else Bedrock
        )
        print(">>>>>>>>>>>>>>>>>>> Question Service Initialized")

    def __generate_questions(self):
        """
        Initializes the question generator and generates questions based on the user input.
        """
        # instantiate the generator class
        __client_instance = self.__client()
        # TODO: Add a layer here, that will produce prompt based on user input difficulty_level, programming_language & topics
        __client_result = __client_instance.generate()
        return __client_result

    def generate_questions(self):
        return self.__generate_questions()


def question_service_obj(
    difficulty_level: str, programming_language: str, topics: dict
):
    question_service_result = QuestionService(
        difficulty_level, programming_language, topics
    ).generate_questions()
    return question_service_result
