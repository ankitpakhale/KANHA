# TODO:
"""
get question generator from .env (OPENAI, AWS BedRock)
get model from .env
"""


class QuestionService:
    def __init__(self, difficulty_level: str, programming_language: str, topics: str):
        self.difficulty_level = difficulty_level
        self.programming_language = programming_language
        self.topics = topics
        print(">>>>>>>>>>>>>>>>>>> Question Service Initialized")

    def generate_questions(self):
        # TODO:
        return [
            {
                "question": "What is the correct way to initialize an empty array in Python?",
                "options": ["array = []", "array = {}", "array = ()", "array = None"],
                "correct_answer": "array = []",
            },
            {
                "question": "How can you access the third element in an array named 'my_array' in Python?",
                "options": ["my_array[3]", "my_array(3)", "my_array{3}", "my_array[2]"],
                "correct_answer": "my_array[2]",
            },
            {
                "question": "Which method in Python can be used to add an element to the end of an array?",
                "options": ["append()", "add()", "insert()", "extend()"],
                "correct_answer": "append()",
            },
            {
                "question": "What will be the output of the following code snippet?\nmy_array = [1, 2, 3]\nprint(my_array[1:])",
                "options": ["[1]", "[2]", "[2, 3]", "[1, 2]"],
                "correct_answer": "[2, 3]",
            },
            {
                "question": "In Python, how can you find the index of a specific element in an array?",
                "options": ["index()", "find()", "search()", "locate()"],
                "correct_answer": "index()",
            },
            {
                "question": "Which of the following is the correct way to copy an array named 'source' to a new array 'target' in Python?",
                "options": [
                    "target = source.copy()",
                    "target = source",
                    "target = copy(source)",
                    "target = source.clone()",
                ],
                "correct_answer": "target = source.copy()",
            },
            {
                "question": "What is the output of the following code snippet?\nmy_array = [4, 2, 7, 1]\nmy_array.sort()\nprint(my_array)",
                "options": [
                    "[1, 2, 4, 7]",
                    "[7, 4, 2, 1]",
                    "[4, 2, 7, 1]",
                    "[1, 7, 2, 4]",
                ],
                "correct_answer": "[1, 2, 4, 7]",
            },
            {
                "question": "Which method in Python can be used to remove the last element from an array?",
                "options": ["pop()", "remove()", "delete()", "clear()"],
                "correct_answer": "pop()",
            },
            {
                "question": "What does the 'len()' function in Python return when used with an array?",
                "options": [
                    "Total number of elements",
                    "Sum of elements",
                    "Average of elements",
                    "Maximum element",
                ],
                "correct_answer": "Total number of elements",
            },
            {
                "question": "In Python, how can you reverse the order of elements in an array 'my_array'?",
                "options": [
                    "my_array.reverse()",
                    "reverse(my_array)",
                    "my_array = my_array[::-1]",
                    "my_array = reverse(my_array)",
                ],
                "correct_answer": "my_array.reverse()",
            },
        ]


def question_service_obj(difficulty_level: str, programming_language: str, topics: str):
    question_service_result = QuestionService(
        difficulty_level, programming_language, topics
    ).generate_questions()
    return question_service_result
