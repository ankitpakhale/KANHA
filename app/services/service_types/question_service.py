from typing import Union, List, Dict
from app.clients import Client
from app.services import validation_manager_obj
import json
from app.utils import logger
from uuid import uuid4
from app.dao import (
    MultipleChoiceQuestion,
    ProblemSolvingQuestion,
    db_session,
)  # noqa: E402


# TODO: change name to GenerateQuestions
class QuestionService:
    @staticmethod
    def __validate_request_data(payload: Dict[str, Union[str, List[str]]]) -> None:
        __validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="request"
        )
        __validation_manager.validate(payload)
        logger.debug("Payload varified successfully at Question Service!!!")

    @staticmethod
    def __get_data_from_client(
        payload: Dict[str, Union[str, List[str]]]
    ) -> List[Dict[str, Union[str, List[Union[str, Dict[str, str]]]]]]:
        __client_response = Client().generate_questions(payload)
        logger.debug(f"Received Questions from Client: {__client_response}")
        return __client_response

    @staticmethod
    def __validate_response_data(response: List[Dict[str, str]]) -> None:
        __validation_manager = validation_manager_obj(
            service_type="generate_questions", validation_type="response"
        )
        for res in response:
            __validation_manager.validate(res)
        logger.debug("Response varified successfully at Question Service!!!")

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
        return __response

    @staticmethod
    def __save_client_response(
        payload: Dict[str, Union[str, List[str]]], response: List[Dict[str, str]]
    ) -> None:
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

    def __generate_questions(self, payload: Dict[str, Union[str, List[str]]]):
        """
        Initializes the question client and generates questions based on the user input.
        """
        # validate the data
        self.__validate_request_data(payload)
        logger.debug("User request data validated at question service")

        # get data from appropriate client and parse the JSON
        __client_response = self.__get_data_from_client(payload)
        logger.debug("Client data received at question service")

        # __client_response = [{'problem_description': 'What is the time complexity of the binary search algorithm?', 'options': ['O(n)', 'O(log n)', 'O(n^2)', 'O(1)'], 'correct_answer': 'O(log n)'}, {'problem_description': 'When would you use a breadth-first search (BFS) algorithm over a depth-first search (DFS) algorithm?', 'options': ['When finding the shortest path in an unweighted graph', 'When memory usage is a concern', 'When the graph is cyclic', 'When the graph is directed'], 'correct_answer': 'When finding the shortest path in an unweighted graph'}, {'problem_description': "What is the purpose of the 'yield' keyword in Python?", 'options': ['To return a value from a function', 'To define a generator function', 'To raise an exception', 'To break out of a loop'], 'correct_answer': 'To define a generator function'}, {'problem_description': 'How can you reverse a list in Python using slicing?', 'options': ['list[::-1]', 'list.reverse()', 'reversed(list)', 'list.reverse(0, len(list))'], 'correct_answer': 'list[::-1]'}, {'problem_description': "What is the output of '2' + '3' in Python?", 'options': ['5', '23', '32', 'Error'], 'correct_answer': '23'}, {'problem_description': 'What is the time complexity of the quicksort algorithm in the best case?', 'options': ['O(n)', 'O(n log n)', 'O(n^2)', 'O(log n)'], 'correct_answer': 'O(n log n)'}, {'problem_description': "What is the purpose of using 'self' in Python class methods?", 'options': ['To refer to the current instance of the class', 'To create a new instance of the class', 'To access class attributes', 'To define a static method'], 'correct_answer': 'To refer to the current instance of the class'}, {'problem_description': "What does the 'pass' statement do in Python?", 'options': ['Exits the loop', 'Continues to the next iteration of the loop', 'Does nothing', 'Raises an exception'], 'correct_answer': 'Does nothing'}, {'problem_description': 'How can you check if a key exists in a Python dictionary?', 'options': ["Using the 'search' method", "Using 'in' keyword", "Using 'exists' function", "Using 'has_key' method"], 'correct_answer': "Using 'in' keyword"}, {'problem_description': "What is the output of 'Hello, World!'[3:] in Python?", 'options': ['Hello', 'World!', 'lo, World!', 'lo, World'], 'correct_answer': 'lo, World!'}, {'problem_description': 'What is the time complexity of the binary search algorithm?', 'options': ['O(n)', 'O(log n)', 'O(n log n)', 'O(1)'], 'correct_answer': 'O(log n)'}, {'problem_description': 'Which data structure is typically used to implement a LIFO behavior?', 'options': ['Queue', 'Heap', 'Stack', 'Linked List'], 'correct_answer': 'Stack'}, {'problem_description': 'In Python, what is the output of the following code snippet?\n\n```python\na = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)\n```', 'options': ['[1, 2, 3]', '[1, 2, 3, 4]', '[1, 2, 4]', '[1, 2, 3, 4, 4]'], 'correct_answer': '[1, 2, 3, 4]'}, {'problem_description': "What is the purpose of the 'pass' statement in Python?", 'options': ['To exit a loop', 'To skip the current iteration in a loop', 'To define an empty function or class', 'To raise an exception'], 'correct_answer': 'To define an empty function or class'}, {
        #     'problem_description': 'Which sorting algorithm has the best worst-case time complexity?', 'options': ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Selection Sort'], 'correct_answer': 'Merge Sort'}, {'problem_description': 'What is the output of the following Python code?\n\n```python\nprint(2 ** 3 ** 2)\n```', 'options': ['64', '512', '72', '9'], 'correct_answer': '512'}, {'problem_description': 'When is it appropriate to use a breadth-first search (BFS) algorithm over a depth-first search (DFS) algorithm?', 'options': ['When finding the shortest path in an unweighted graph', 'When memory consumption is a concern', 'When the graph is cyclic', 'When the graph is sparse'], 'correct_answer': 'When finding the shortest path in an unweighted graph'}, {'problem_description': 'What is the time complexity of the quicksort algorithm in the best-case scenario?', 'options': ['O(n)', 'O(n log n)', 'O(n^2)', 'O(log n)'], 'correct_answer': 'O(n log n)'}, {'problem_description': "In Python, what will be the output of the following code snippet?\n\n```python\nprint(' '.join([str(i) for i in range(5)]))\n```", 'options': ['0 1 2 3 4', '1 2 3 4 5', '0 1 2 3', '1 2 3 4'], 'correct_answer': '0 1 2 3 4'}, {'problem_description': 'What is the key difference between a set and a frozenset in Python?', 'options': ['A set is mutable while a frozenset is immutable', 'A set allows duplicate elements while a frozenset does not', 'A frozenset can be converted to a list but a set cannot', 'A set is ordered while a frozenset is unordered'], 'correct_answer': 'A set is mutable while a frozenset is immutable'}, {'problem_description': 'What is the time complexity of the binary search algorithm?', 'options': ['O(n)', 'O(log n)', 'O(n^2)', 'O(1)'], 'correct_answer': 'O(log n)'}, {'problem_description': 'Explain the difference between list and tuple in Python.', 'input_format': 'N/A', 'output_format': 'N/A', 'constraints': 'N/A', 'examples': [{'input': 'N/A', 'output': 'N/A'}], 'edge_cases': [{'input': 'N/A', 'output': 'N/A'}]}, {'problem_description': 'Write a Python function to check if a string is a palindrome.', 'input_format': 'A string input.', 'output_format': 'Return True if the string is a palindrome, False otherwise.', 'constraints': 'Assume the input string contains only alphabetic characters and no spaces.', 'examples': [{'input': "'radar'", 'output': 'True'}, {'input': "'hello'", 'output': 'False'}], 'edge_cases': [{'input': "'A man, a plan, a canal, Panama!'", 'output': 'True'}, {'input': "'race a car'", 'output': 'False'}]}, {'problem_description': "What is the difference between '==' and 'is' in Python?", 'options': ['Both are used for value comparison.', "'==' is used for reference comparison, 'is' is used for value comparison.", "'==' is used for value comparison, 'is' is used for reference comparison.", "'==' and 'is' are interchangeable in Python."], 'correct_answer': "'==' is used for value comparison, 'is' is used for reference comparison."}, {'problem_description': 'Explain the concept of list comprehension in Python with an example.', 'input_format': 'N/A', 'output_format': 'N/A', 'constraints': 'N/A', 'examples': [{'input': 'N/A', 'output': 'N/A'}], 'edge_cases': [{'input': 'N/A', 'output': 'N/A'}]}]

        # validate client response
        self.__validate_response_data(__client_response)
        logger.debug("Client response data validated at question service")

        # add q_id in all the questions
        __formatted_json_with_id = self.__add_id_in_response(__client_response)
        logger.debug("Added IDs in validated client data at question service")

        # save client response in DB
        self.__save_client_response(payload, __formatted_json_with_id)
        logger.debug("Saved client data in DB at question service")

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
