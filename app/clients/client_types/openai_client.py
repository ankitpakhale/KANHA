from typing import Optional, List, Dict, Union
from app.clients import Base
import openai
from app.config import OpenAIConfig
from app.utils import logger
import json
from app.utils import ClientSettings
from math import ceil
import re


class OpenAI(Base):
    def __init__(self) -> None:
        # config data
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = OpenAIConfig.OPENAI_TEMPERATURE
        self.max_tokens = OpenAIConfig.OPENAI_MAX_TOKENS
        self.batch_size = ClientSettings.BATCH_SIZE

    @staticmethod
    def __fix_raw_response(json_str: str) -> str:
        """
        Fixes a potentially malformed JSON string by:
        - Ensuring proper double quotes for keys and string values.
        - Handling special characters and structural issues.
        """
        try:
            # attempt to load the JSON as-is to see if it's valid
            loaded_json = json.loads(json_str)
            question_list = []
            if "questions" in loaded_json:
                logger.warning("question key detected in json data.")
                question_list.extend(loaded_json["questions"])
            if "Easy" in loaded_json and loaded_json["Easy"] is not None:
                logger.warning("Easy key detected in json data.")
                question_list.extend(loaded_json["Easy"])
            if "Medium" in loaded_json and loaded_json["Medium"] is not None:
                logger.warning("Medium key detected in json data.")
                question_list.extend(loaded_json["Medium"])
            if "Hard" in loaded_json and loaded_json["Hard"] is not None:
                logger.warning("Hard key detected in json data.")
                question_list.extend(loaded_json["Hard"])
            logger.info(
                "Received JSON is by default complient with json.loads, returning the json data."
            )
            return question_list
        except json.JSONDecodeError:
            logger.error("JSONDecodeError Occured, continue fixing the JSON...")
            pass  # continue fixing the JSON

        # use regex to remove comments and other invalid structures
        # remove single-line comments starting with #
        if "#" in json_str:
            logger.warning("Comments detected, removing comments from the JSON.")
            try:
                json_str = re.sub(r"#.*$", "", json_str, flags=re.MULTILINE)
                logger.debug("Detected comments removed, loading the JSON.")
                loaded_json = json.loads(json_str)
                logger.info(
                    "Received JSON is by default complient with json.loads, returning the json data."
                )
                return loaded_json
            except json.JSONDecodeError:
                logger.error(
                    "JSONDecodeError Occured while removing the comment, continue fixing the JSON..."
                )
                pass  # continue fixing the JSON

        # use regex to extract the list
        matches = re.search(r"\[\s*(\{.*?\})\s*\]", json_str, re.DOTALL)
        if matches:
            # extract the JSON string
            json_str = f"[{matches.group(1)}]"

        # replace single quotes with double quotes for JSON compatibility
        json_str = json_str.replace("'", '"')

        # fix invalid spacing and formatting issues
        json_str = re.sub(r"\s*:\s*", ":", json_str)
        json_str = re.sub(r"\s*,\s*", ",", json_str)

        # ensure keys are properly quoted
        json_str = re.sub(r'(?<=\{|,)\s*([^"\s][^:]+)\s*:', r'"\1":', json_str)

        # Fix improperly escaped quotes within strings
        json_str = re.sub(r'(?<!\\)"(?![:,\]}])', r'\\"', json_str)

        # ensure proper array/object separation
        json_str = re.sub(r"}\s*{", r"},{", json_str)

        # remove trailing commas
        json_str = re.sub(r",(?=\s*[}\]])", "", json_str)

        # strip invalid leading/trailing characters
        json_str = json_str.strip()
        logger.info(f"Applied string operations in stringified json: {json_str}")
        return json.loads(json_str)

    def __get_result(self, system_prompt: str, user_prompt: str) -> str:
        # call openai to result based on requested prompt
        __response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        # extract and return the results
        __result = __response["choices"][0]["message"]["content"]
        logger.info("Received result from OpenAI Client")
        return __result

    def __get_batch_result(self, payload):
        """ """
        difficulty_level = payload["difficulty_level"]
        programming_language = payload["programming_language"]
        topics = ", ".join(payload["topics"])
        num_questions = payload.get(
            "num_questions", 25
        )  # specify any number, default is 20

        print("➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ")
        print("➡ difficulty_level:", difficulty_level)
        print("➡ programming_language:", programming_language)
        print("➡ topics:", topics)
        print("➡ num_questions:", num_questions)
        print("➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ")

        result = []
        num_calls = 0  # keep track of total calls

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
            json_string = self.__get_result(
                system_prompt=system_prompt, user_prompt=user_prompt
            )
            logger.debug(f"json_string: {json_string}")

            response = self.__fix_raw_response(json_string)
            logger.debug(f"response: {response}")

            result.extend(response)
            num_calls += current_batch_size

        return result

    def generate_questions(self, payload: Union[list, dict]) -> str:
        """
        Core logic to generate questions from OpenAI client
        """
        logger.debug("generate_questions core logic working for OpenAI client")
        response = self.__get_batch_result(payload)
        logger.debug("Received generated questions from OpenAI Client")
        return response

    def evaluate_answers(self, payload: Union[list, dict]) -> str:
        """
        Core logic to evaluate users answer using OpenAI client
        """
        logger.debug("evaluate_answers core logic working for OpenAI client")
        __system_prompt = self.get_answer_evaluation_system_prompt(user_code=payload)
        __user_prompt = self.get_answer_evaluation_user_prompt(user_code=payload)
        __evaluation = self.__get_result(
            system_prompt=__system_prompt, user_prompt=__user_prompt
        )
        logger.debug("Received evaluated answers from OpenAI Client")
        return __evaluation
