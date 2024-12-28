from typing import Optional, List, Dict, Union
from clients import Base
import openai
from config import OpenAIConfig
from typeguard import typechecked
from utils import logger
import json

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.memory import ConversationBufferMemory


class OpenAI(Base):
    def __init__(self) -> None:
        # config data
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = OpenAIConfig.OPENAI_TEMPERATURE
        self.max_tokens = OpenAIConfig.OPENAI_MAX_TOKENS
        # self.text_splitter = RecursiveCharacterTextSplitter(
        #     chunk_size=3000, chunk_overlap=100)
        # self.memory = ConversationBufferMemory()

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
        logger.debug(f"➡ 28 __response: {__response}")

        # extract and return the results
        __result = __response["choices"][0]["message"]["content"]
        logger.info("Received result from OpenAI Client")
        return __result

    # def __validate_and_combine_json(responses: List[str]) -> Dict:
    #     combined_result = {}
    #     for response in responses:
    #         try:
    #             partial_result = json.loads(response)
    #             combined_result.update(partial_result)
    #         except json.JSONDecodeError as e:
    #             logger.error(f"Invalid JSON: {response}. Error: {e}")
    #     return combined_result

    # def __get_result__new(self, system_prompt: str, user_prompt: str) -> str:
    #     """
    #     Use LangChain to handle long prompts and chunk input while maintaining context.
    #     """
    #     chunks = self.text_splitter.split_text(user_prompt)
    #     logger.debug(f"Split user prompt into {len(chunks)} chunks.")

    #     responses = []
    #     for chunk in chunks:
    #         logger.debug(f"Getting result for chunk: {chunks}")

    #         # add memory-based conversation context
    #         conversation_context = self.memory.chat_memory.messages
    #         logger.debug(f"Conversation Context: {conversation_context}")

    #         # prepare messages with context
    #         messages = [
    #             {"role": "system", "content": system_prompt},
    #             *conversation_context,  # add past conversation
    #             {"role": "user", "content": chunk},
    #         ]

    #         # calculate the number of tokens used in input
    #         # total_available_tokens = 4096  # total limit for GPT-3.5 Turbo
    #         # total_input_tokens = sum(len(m["content"])
    #         #                         for m in messages)  # input tokens used
    #         # if total_input_tokens + self.max_tokens > total_available_tokens:
    #         #     # truncate old context if tokens exceed the limit
    #         #     logger.warning(f"messages exceed token limit , truncating context...")
    #         #     self.memory.clear()  # clear old memory to make space

    #         # call OpenAI API
    #         response = openai.ChatCompletion.create(
    #             model=self.model,
    #             messages=messages,
    #             temperature=self.temperature,
    #             max_tokens=self.max_tokens,
    #         )
    #         result = response["choices"][0]["message"]["content"]
    #         self.memory.save_context({"input": chunk}, {"output": result})
    #         responses.append(result)

    #     # combine and validate JSON
    #     final_output = self.__validate_and_combine_json(responses)
    #     logger.info("Received final result from OpenAI Client")
    #     return final_output

    @typechecked
    def generate_questions(self, payload: Union[list, dict]) -> str:
        """
        Core logic to generate questions from OpenAI client
        """
        logger.info("generate_questions core logic working for OpenAI client")
        difficulty_level = payload["difficulty_level"]
        programming_language = payload["programming_language"]
        topics = payload["topics"]
        num_questions = payload.get(
            "num_questions", 2
        )  # specify any number, default is 20

        __system_prompt = self.get_question_generation_system_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=", ".join(topics),
            num_questions=num_questions,
        )
        __user_prompt = self.get_question_generation_user_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=", ".join(topics),
            num_questions=num_questions,
        )
        logger.debug(f"Generating Questions for __user_prompt: {__user_prompt}")
        __generation = self.__get_result(
            system_prompt=__system_prompt, user_prompt=__user_prompt
        )

        logger.info("Received generated questions from OpenAI Client")
        return __generation

    @typechecked
    def evaluate_answers(self, payload: Union[list, dict]) -> str:
        """
        Core logic to evaluate users answer using OpenAI client
        """
        logger.info("evaluate_answers core logic working for OpenAI client")
        __system_prompt = self.get_answer_evaluation_system_prompt(user_code=payload)
        __user_prompt = self.get_answer_evaluation_user_prompt(user_code=payload)
        __evaluation = self.__get_result(
            system_prompt=__system_prompt, user_prompt=__user_prompt
        )
        logger.info("Received evaluated answers from OpenAI Client")
        return __evaluation
