class AWSBedrockClient:
    def __init__(self):
        print(">>>>>>>>>>>>>>>>>>> AWSBedrockClient is Ready!!!")

    def __generate(self):
        return [
            {
                "q_type": "MCQ",
                "question": "What is the correct way to initialize an empty array in Python?",
                "options": ["array = []", "array = {}", "array = ()", "array = None"],
                "correct_answer": "array = []",
            },
            {
                "q_type": "MCQ",
                "question": "How can you access the third element in an array named 'my_array' in Python?",
                "options": ["my_array[3]", "my_array(3)", "my_array{3}", "my_array[2]"],
                "correct_answer": "my_array[2]",
            },
            {
                "q_type": "MCQ",
                "question": "Which method in Python can be used to add an element to the end of an array?",
                "options": ["append()", "add()", "insert()", "extend()"],
                "correct_answer": "append()",
            },
            {
                "q_type": "MCQ",
                "question": "What will be the output of the following code snippet?\nmy_array = [1, 2, 3]\nprint(my_array[1:])",
                "options": ["[1]", "[2]", "[2, 3]", "[1, 2]"],
                "correct_answer": "[2, 3]",
            },
            {
                "q_type": "MCQ",
                "question": "In Python, how can you find the index of a specific element in an array?",
                "options": ["index()", "find()", "search()", "locate()"],
                "correct_answer": "index()",
            },
            {
                "q_type": "MCQ",
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
                "q_type": "MCQ",
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
                "q_type": "MCQ",
                "question": "Which method in Python can be used to remove the last element from an array?",
                "options": ["pop()", "remove()", "delete()", "clear()"],
                "correct_answer": "pop()",
            },
            {
                "q_type": "MCQ",
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
                "q_type": "MCQ",
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

    def generate(self):
        return self.__generate()
