from config import GeneralConfig
from clients import AWSBedrockClient, OpenAIClient


class QuestionService:
    def __init__(self, difficulty_level: str, programming_language: str, topics: str):
        self.__difficulty_level = difficulty_level
        self.__programming_language = programming_language
        self.__topics = topics
        self.__generator = (
            OpenAIClient
            if GeneralConfig.Q_GENERATOR == OpenAIClient.__name__
            else AWSBedrockClient
        )
        print(">>>>>>>>>>>>>>>>>>> Question Service Initialized")

    def __generate_questions(self):
        """
        Initializes the question generator and generates questions based on the user input.
        """
        # instantiate the generator class
        __generator_instance = self.__generator()
        # TODO: Add a layer here, that will produce prompt based on user input difficulty_level, programming_language & topics
        __generator_result = __generator_instance.generate()
        return __generator_result

    def generate_questions(self):
        return self.__generate_questions()


def question_service_obj(difficulty_level: str, programming_language: str, topics: str):
    question_service_result = QuestionService(
        difficulty_level, programming_language, topics
    ).generate_questions()
    return question_service_result
