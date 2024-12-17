import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# validation_manager import should be after path adjustments only
from validation_manager import validation_manager_obj

GENERATE_QUESTIONS = "generate_questions"
EVALUATE_ANSWERS = "evaluate_answers"
REQUEST = "request"
RESPONSE = "response"

PAYLOAD_MAP = {
    GENERATE_QUESTIONS: {
        REQUEST: {
            "difficulty_level": "medium",
            "programming_language": "python",
            "topics": ["data structures", "algorithms"],
        },
        RESPONSE: [
            {
                "q_id": "mcq01223211122",
                "question": "In Python, which loop is used when a specific condition needs to be checked before each iteration?",
                "options": ["for loop", "while loop", "do-while loop", "foreach loop"],
                "correct_answer": "while loop",
            },
            {
                "q_id": "mcq01293211122",
                "question": "Which keyword is used to define a function in Python?",
                "options": ["method", "def", "func", "define"],
                "correct_answer": "def",
            },
        ],
    },
    EVALUATE_ANSWERS: {
        REQUEST: [
            {
                "q_id": "psq01223211122",
                "problem_description": "Write a Python function that takes a list of integers and returns the maximum product of three numbers from the list. The function should handle both positive and negative integers.",
                "input_format": "Input consists of a list of integers.",
                "output_format": "Output should be an integer representing the maximum product of three numbers.",
                "constraints": "The length of the list will be at least 3 and at most 10^4. Integers in the list will be in the range [-1000, 1000].",
                "examples": [
                    {"input": "[1, 2, 3, 4, 5]", "output": "60"},
                    {"input": "[-10, -5, 1, 2, 3]", "output": "150"},
                ],
                "edge_cases": [
                    {"input": "[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]", "output": "125"}
                ],
                "user_code": "def max_product(nums):\n    nums.sort()\n    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])",
            },
            {
                "q_id": "psq01293211122",
                "problem_description": "Implement a Python function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.",
                "input_format": "Input consists of an array of strings.",
                "output_format": "Output should be a string representing the longest common prefix.",
                "constraints": "The number of strings in the array will be at least 1 and at most 200. The length of each string will be at most 200.",
                "examples": [
                    {"input": '["flower", "flow", "flight"]', "output": '"fl"'},
                    {"input": '["dog", "racecar", "car"]', "output": '""'},
                ],
                "edge_cases": [
                    {"input": '["apple", "app", "application"]', "output": '"app"'}
                ],
                "user_code": 'def longestCommonPrefix(strs):\n    if not strs:\n        return ""\n    \n    # Start by assuming the first string is the prefix\n    prefix = strs[0]\n    \n    # Loop through the strings\n    for string in strs[1:]:\n        # Update the prefix while it\'s not a prefix of the current string\n        while not string.startswith(prefix):\n            prefix = prefix[:-1]\n            if not prefix:\n                return ""\n    \n    return prefix',
            },
        ],
        RESPONSE: [
            {
                "q_id": "psq01223211122",
                "feedback": [
                    {
                        "correctness": "The function correctly finds the maximum product of three numbers from the list. It handles both positive and negative integers by sorting the list and considering the cases where the maximum product can be achieved by multiplying the two smallest numbers with the largest number or by multiplying the three largest numbers."
                    },
                    {
                        "areas_for_improvement": "1. The function does not handle the case where the list contains both negative and positive integers. In such cases, the maximum product can be achieved by either multiplying the three largest positive numbers or by multiplying the two smallest (most negative) numbers with the largest positive number. This case is not considered in the current implementation.\n2. The function sorts the entire list, which has a time complexity of O(nlogn). This can be improved by finding the three largest numbers and two smallest numbers in a single pass through the list, which would have a time complexity of O(n).\n3. The function could benefit from more descriptive variable names for better readability."
                    },
                    {
                        "strengths": "The function correctly handles cases where the maximum product is achieved by either multiplying the two smallest numbers with the largest number or by multiplying the three largest numbers. The code is concise and easy to understand."
                    },
                ],
                "points": "4",
            },
            {
                "q_id": "psq01293211122",
                "feedback": [
                    {
                        "correctness": "The function correctly finds the longest common prefix string amongst an array of strings. It handles the case where there is no common prefix and returns an empty string."
                    },
                    {
                        "areas_for_improvement": "1. The function could be optimized by using the zip function to compare characters of the strings simultaneously instead of iterating character by character.\n2. The variable name 'strs' could be more descriptive to indicate that it represents an array of strings.\n3. The comment '# Start by assuming the first string is the prefix' is misleading as it actually assigns the first string as the prefix, not assumes it."
                    },
                    {
                        "strengths": "The function correctly handles finding the longest common prefix and the case where there is no common prefix. The code is structured and easy to follow."
                    },
                ],
                "points": "7",
            },
        ],
    },
}

__service_list = [
    GENERATE_QUESTIONS,
    EVALUATE_ANSWERS,
]
__validation_list = [
    REQUEST,
    RESPONSE,
]
__service_type = __service_list[0]
__validation_type = __validation_list[1]

__payload = PAYLOAD_MAP[__service_type][__validation_type]

is_valid = validation_manager_obj(
    service_type=__service_type, validation_type=__validation_type
).validate(__payload)
print("➡ is_valid:", is_valid)
