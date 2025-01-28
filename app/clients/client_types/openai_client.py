# external libraries
from typing import Optional, List, Dict, Union, Any
import json
from math import ceil
import re

# langchain libraries
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import messages_to_dict
from langchain_openai import ChatOpenAI
from langchain_core.exceptions import OutputParserException
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# local imports
from app.clients import Base
from app.config import OpenAIConfig
from app.utils import logger
from app.utils import ClientSettings


class OpenAIClient(Base):
    def __init__(self) -> None:
        # config data
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = OpenAIConfig.OPENAI_TEMPERATURE
        self.max_tokens = OpenAIConfig.OPENAI_MAX_TOKENS
        self.batch_size = ClientSettings.BATCH_SIZE

        # initialize message history for context
        self.message_history = ChatMessageHistory()
        self.llm = ChatOpenAI(
            model=self.model, temperature=self.temperature, max_tokens=self.max_tokens
        )

    @staticmethod
    def __prepare_context_content(response: list) -> str:
        # extract problem_descriptions
        problem_descriptions = [
            item["problem_description"]
            for item in response
            if "problem_description" in item
        ]
        return "\n".join(problem_descriptions)

    def __update_context(self, content: str) -> None:
        """
        adds a message to the context message history
        """
        self.message_history.add_message(content)

    def __prepare_combined_prompt(
        self, system_prompt: str, user_prompt: str
    ) -> List[Dict[str, str]]:
        """
        prepares the combined prompt using system prompt, user prompt, and context
        """
        # fetch context as a list of messages
        context = messages_to_dict(self.message_history.messages)
        # combine system prompt, context, and user prompt
        combined_prompt = (
            [{"role": "system", "content": system_prompt}]
            + context
            + [{"role": "user", "content": user_prompt}]
        )
        return combined_prompt

    @staticmethod
    def __fix_raw_response(json_str: str) -> str:
        """
        fixes a potentially malformed JSON string
        """
        try:
            loaded_json = json.loads(json_str)
            question_list = []

            # define keys to look for and check them
            question_keys = ["questions", "Easy", "Medium", "Hard"]
            for key in question_keys:
                if key in loaded_json and loaded_json[key]:
                    logger.warning(f"{key} key detected in json data.")
                    question_list.extend(loaded_json["questions"])
            logger.info(
                "received json is compliant with json.loads, returning the json data."
            )
            return question_list
        except json.JSONDecodeError:
            logger.error("jsondecodeerror occured, continue fixing the json...")
            pass  # continue fixing the json

        # additional json cleanup operations
        if "#" in json_str:
            logger.warning("comments detected, removing comments from the json.")
            try:
                json_str = re.sub(r"#.*$", "", json_str, flags=re.MULTILINE)
                loaded_json = json.loads(json_str)
                logger.info(
                    "received json is compliant with json.loads, returning the json data."
                )
                return loaded_json
            except json.JSONDecodeError:
                logger.error(
                    "jsondecodeerror occured while removing comments, continue fixing the json..."
                )
                pass  # continue fixing the json

        matches = re.search(r"\[\s*(\{.*?\})\s*\]", json_str, re.DOTALL)
        if matches:
            json_str = f"[{matches.group(1)}]"

        # replace single quotes with double quotes for json compatibility
        json_str = json_str.replace("'", '"')

        # fix invalid spacing and formatting issues
        json_str = re.sub(r"\s*:\s*", ":", json_str)
        json_str = re.sub(r"\s*,\s*", ",", json_str)

        json_str = re.sub(r'(?<=\{|,)\s*([^"\s][^:]+)\s*:', r'"\1":', json_str)
        json_str = re.sub(r'(?<!\\)"(?![:,\]}])', r'\\"', json_str)
        json_str = re.sub(r"}\s*{", r"},{", json_str)
        json_str = re.sub(r",(?=\s*[}\]])", "", json_str)

        json_str = json_str.strip()
        logger.info(f"applied string operations in stringified json: {json_str}")
        return json.loads(json_str)

    @staticmethod
    def __parse_json_with_langchain(raw_response: Any) -> Any:
        """
        Parse the raw response using LangChain's structured output parser
        to extract questions or problem descriptions in a structured format.
        This function ensures the response is in string format before attempting to parse it.
        """
        # TODO: Adjust __parse_json_with_langchain method according to both questions generation and evaluate answers
        # Check if the response is an AIMessage object and extract content if it is
        if hasattr(raw_response, "content"):
            raw_response = (
                raw_response.content
            )  # Extract the content from the AIMessage object

        logger.debug(f"➡ raw_response: {raw_response}")
        # Convert the raw response (string) to a dictionary using json.loads
        try:
            raw_response = json.loads(raw_response)
        except json.JSONDecodeError:
            raise OutputParserException(
                f"Failed to parse the raw response as JSON. Received: {type(raw_response)}"
            )

        question_list = []

        for _type in ["questions", "Easy", "Medium", "Hard"]:
            if isinstance(raw_response, dict) and _type in raw_response:
                # Extract list from the _type key
                raw_response = raw_response[_type]
                question_list.extend(raw_response)
                print("➡ questions key raw_response:", raw_response)
        else:
            question_list.extend(raw_response)

        print("➡ FINAL question_list:", question_list)
        return question_list

        # # Check if the response is already in the expected list format
        # if not isinstance(raw_response, list):
        #     raise OutputParserException(
        #         f"Expected a list of questions, but got: {type(raw_response)}")

        # # Define the expected structure of the response for both problem descriptions and questions
        # problem_description_schema = ResponseSchema(
        #     name="problem_description",
        #     description="Detailed problem description with input/output/constraints, examples, and edge cases."
        # )

        # question_schema = ResponseSchema(
        #     name="question",
        #     description="Multiple choice question with options and correct answer."
        # )

        # # Define a new schema for both types of data
        # mixed_schema = ResponseSchema(
        #     name="mixed_type",
        #     description="Can be either a problem description with examples/edge cases or a multiple choice question."
        # )

        # # Use StructuredOutputParser to handle both types of responses
        # parser = StructuredOutputParser.from_response_schemas(
        #     # Add mixed_schema to handle both types
        #     [problem_description_schema, question_schema, mixed_schema])

        # try:
        #     # Use LangChain's parsing utility to extract structured data
        #     parsed_response = parser.parse(raw_response)
        #     logger.debug(f"Parsed response: {parsed_response}")
        #     return parsed_response  # Return parsed response that could be any type
        # except Exception as e:
        #     logger.error(f"Error parsing response with LangChain: {e}")
        #     raise ValueError("Error parsing response with LangChain")

    def __get_result(self, system_prompt: str, user_prompt: str) -> str:
        # prepare combined prompt
        combined_prompt = self.__prepare_combined_prompt(system_prompt, user_prompt)

        # generate response using langchain's chatopenai
        raw_response = self.llm.invoke(combined_prompt)
        logger.debug(f"➡ raw_response: {raw_response}")

        return raw_response

    def __get_batch_result(self, payload):
        """
        retrieves questions or problem descriptions in batches and maintains context
        """
        difficulty_level = payload["difficulty_level"]
        programming_language = payload["programming_language"]
        topics = payload["topics"]
        num_questions = payload.get("num_questions", 2)

        result = []
        num_calls = 0  # track number of api calls

        system_prompt = self.get_question_generation_system_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        )

        for _ in range(ceil(num_questions / self.batch_size)):
            current_batch_size = min(self.batch_size, num_questions - num_calls)
            user_prompt = self.get_question_generation_user_prompt(
                difficulty_level=difficulty_level,
                programming_language=programming_language,
                topics=topics,
                num_questions=current_batch_size,
            )

            raw_response = self.__get_result(
                system_prompt=system_prompt, user_prompt=user_prompt
            )

            # call the new LangChain parsing method to extract questions or problem descriptions
            response = self.__parse_json_with_langchain(raw_response)

            self.__update_context(content=self.__prepare_context_content(response))

            result.extend(response)
            num_calls += current_batch_size
            print(">" * 80)
            print(f"One Iteration completed, the result is {result}")
            print("<" * 80)
        return result

    def generate_questions(self, payload: Dict[str, str]) -> str:
        """
        core logic to generate questions from openai client
        """
        logger.debug(
            "generate_questions core logic working for openai client with context"
        )
        response = self.__get_batch_result(payload)
        logger.debug("received generated questions from openai client with context")
        return response

    def evaluate_answers(self, payload: Union[list, dict]) -> str:
        """
        core logic to evaluate user answers using openai client
        """
        logger.debug(
            "evaluate_answers core logic working for openai client with context"
        )
        system_prompt = self.get_answer_evaluation_system_prompt(user_code=payload)
        user_prompt = self.get_answer_evaluation_user_prompt(user_code=payload)
        evaluation = self.__get_result(
            system_prompt=system_prompt, user_prompt=user_prompt
        )
        response = self.__parse_json_with_langchain(evaluation)

        logger.debug("received evaluated answers from openai client with context")
        return response
