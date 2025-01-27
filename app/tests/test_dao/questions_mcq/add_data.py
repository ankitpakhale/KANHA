import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import MultipleChoiceQuestion, db_session  # noqa: E402
import random  # noqa: E402

# list of MCQ entries
multiple_choice_question_entries = [
    {
        "difficulty_level": "easy",
        "question": "Which of the following is a valid variable name in Python?",
        "option_1": "1variable",
        "option_2": "variable_1",
        "option_3": "variable-1",
        "option_4": "variable.1",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What is the output of the following code?\nprint(type(10))",
        "option_1": "<class 'float'>",
        "option_2": "<class 'int'>",
        "option_3": "<class 'str'>",
        "option_4": "<class 'bool'>",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following data types is immutable in Python?",
        "option_1": "List",
        "option_2": "Set",
        "option_3": "Dictionary",
        "option_4": "Tuple",
        "correct_answer": "option_4",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What is the correct syntax to create a dictionary in Python?",
        "option_1": "d = [1, 2, 3]",
        "option_2": "d = (1, 2, 3)",
        "option_3": "d = {1: 'a', 2: 'b'}",
        "option_4": "d = [1: 'a', 2: 'b']",
        "correct_answer": "option_3",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following functions is used to get the length of a string in Python?",
        "option_1": "size()",
        "option_2": "count()",
        "option_3": "length()",
        "option_4": "len()",
        "correct_answer": "option_4",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What is the result of the following code?\nprint(3 + 2 * 2)",
        "option_1": "7",
        "option_2": "10",
        "option_3": "5",
        "option_4": "9",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which operator is used to divide two numbers in Python?",
        "option_1": "/",
        "option_2": "//",
        "option_3": "%",
        "option_4": "*",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What will be the output of the following code?\nprint('Hello'.lower())",
        "option_1": "hello",
        "option_2": "HELLO",
        "option_3": "Hello",
        "option_4": "Error",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following is used to create an empty list in Python?",
        "option_1": "list()",
        "option_2": "[]",
        "option_3": "{}",
        "option_4": "empty()",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following methods is used to add an element at the end of a list?",
        "option_1": "add()",
        "option_2": "insert()",
        "option_3": "append()",
        "option_4": "extend()",
        "correct_answer": "option_3",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What does the 'len()' function do in Python?",
        "option_1": "Finds the length of a list",
        "option_2": "Finds the length of a string",
        "option_3": "Both of the above",
        "option_4": "None of the above",
        "correct_answer": "option_3",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following is used for looping through a sequence in Python?",
        "option_1": "for loop",
        "option_2": "while loop",
        "option_3": "do-while loop",
        "option_4": "loop",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What is the output of the following code?\nprint('Python' == 'python')",
        "option_1": "True",
        "option_2": "False",
        "option_3": "Error",
        "option_4": "None",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What is the result of the expression 10 % 3 in Python?",
        "option_1": "1",
        "option_2": "3",
        "option_3": "0",
        "option_4": "2",
        "correct_answer": "option_4",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following methods is used to remove an item from a list by index?",
        "option_1": "remove()",
        "option_2": "pop()",
        "option_3": "del()",
        "option_4": "clear()",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What will be the output of the following code?\nprint(2**3)",
        "option_1": "6",
        "option_2": "8",
        "option_3": "9",
        "option_4": "Error",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "What is the default value of a tuple in Python?",
        "option_1": "[]",
        "option_2": "()",
        "option_3": "{}",
        "option_4": "None",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "How do you start a comment in Python?",
        "option_1": "//",
        "option_2": "#",
        "option_3": "/*",
        "option_4": "--",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following is the correct syntax to import a module in Python?",
        "option_1": "import module_name",
        "option_2": "import(module_name)",
        "option_3": "from module_name import *",
        "option_4": "import module_name()",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following is used to declare a function in Python?",
        "option_1": "def",
        "option_2": "function",
        "option_3": "func",
        "option_4": "declare",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which built-in Python module is used to work with regular expressions?",
        "option_1": "regex",
        "option_2": "re",
        "option_3": "regexpr",
        "option_4": "re.regex",
        "correct_answer": "option_2",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "How can you check if a string contains a specific substring in Python?",
        "option_1": "'substring' in string",
        "option_2": "substring('string')",
        "option_3": "string.includes('substring')",
        "option_4": "substring.contains(string)",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "easy",
        "question": "Which of the following is used to concatenate two strings in Python?",
        "option_1": "+",
        "option_2": "&",
        "option_3": "*",
        "option_4": "|",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "medium",
        "question": "What is the output of the following code?\nnums = [1, 2, 3, 4]\nnums[2:4] = [5, 6, 7]\nprint(nums)",
        "option_1": "[1, 2, 5, 6, 7]",
        "option_2": "[1, 2, 5, 6]",
        "option_3": "[1, 2, 3, 4, 5, 6, 7]",
        "option_4": "[1, 2, 5, 6, 7, 4]",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "medium",
        "question": "What will be the output of the following code?\na = {1, 2, 3}\nb = {3, 4, 5}\nprint(a & b)",
        "option_1": "{3}",
        "option_2": "{1, 2, 3, 4, 5}",
        "option_3": "{1, 2}",
        "option_4": "Error",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "medium",
        "question": "Which of the following is the correct way to raise a custom exception in Python?",
        "option_1": "raise Exception()",
        "option_2": "throw Exception()",
        "option_3": "raise CustomError()",
        "option_4": "throw CustomError()",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "medium",
        "question": "What is the output of the following code?\nx = [1, 2, 3]\ny = x\nx.append(4)\nprint(y)",
        "option_1": "[1, 2, 3, 4]",
        "option_2": "[1, 2, 3]",
        "option_3": "Error",
        "option_4": "[4]",
        "correct_answer": "option_1",
        "required_time": "2",
    },
    {
        "difficulty_level": "medium",
        "question": "Which of the following will create a generator in Python?",
        "option_1": "my_gen = (x for x in range(5))",
        "option_2": "my_gen = [x for x in range(5)]",
        "option_3": "my_gen = {x for x in range(5)}",
        "option_4": "my_gen = list(range(5))",
        "correct_answer": "option_1",
        "required_time": "2",
    },
]

# randomly select one feedback entry
selected_mcq = random.choice(multiple_choice_question_entries)

# create the session
session = db_session()

# use the selected entry in mcq_entry
mcq_entry = MultipleChoiceQuestion(
    difficulty_level=selected_mcq["difficulty_level"],
    question=selected_mcq["question"],
    option_1=selected_mcq["option_1"],
    option_2=selected_mcq["option_2"],
    option_3=selected_mcq["option_3"],
    option_4=selected_mcq["option_4"],
    correct_answer=selected_mcq["correct_answer"],
    required_time=selected_mcq["required_time"],
)

# retrieve all feedback entries from the database and print them
mcq_obj = (
    session.query(MultipleChoiceQuestion)
    .filter(MultipleChoiceQuestion.question == mcq_entry.question)
    .all()
)

if not mcq_obj:
    session.add(mcq_entry)
    session.commit()
    print("\n=====================> MCQ Data added successfully!!!\n")

    print(mcq_entry)

else:
    print("\n=====================> This Question is already Added!!!\n")
    for obj in mcq_obj:
        print(obj)
