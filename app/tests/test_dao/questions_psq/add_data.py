import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import ProblemSolvingQuestion, db_session  # noqa: E402
import random  # noqa: E402

problem_solvinge_question_entries = [
    {
        "q_id": "psq00123456789",
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
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq00234567890",
        "problem_description": "Write a Python function that checks if a given string is a palindrome, ignoring spaces and punctuation.",
        "input_format": "Input is a string containing only alphabetical characters and spaces.",
        "output_format": "Output should be a boolean value, True if the string is a palindrome, otherwise False.",
        "constraints": "The length of the string will be at most 10^5 characters.",
        "examples": [
            {"input": "A man a plan a canal Panama", "output": "True"},
            {"input": "Hello World", "output": "False"},
        ],
        "edge_cases": [
            {"input": "Madam", "output": "True"},
            {"input": " ", "output": "True"},
        ],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq00345678901",
        "problem_description": "Write a Python function that finds the shortest path in a graph from a source node to a destination node. You may assume the graph is represented as an adjacency matrix.",
        "input_format": "The input consists of an integer n (the number of nodes) and an n x n adjacency matrix where each element represents the distance between nodes. The source and destination nodes are also given as integers.",
        "output_format": "Output should be the length of the shortest path between the source and destination nodes.",
        "constraints": "The number of nodes, n, will be between 2 and 100. The graph will not contain negative weights.",
        "examples": [
            {
                "input": "4\n[[0, 10, 15, 0], [10, 0, 35, 25], [15, 35, 0, 30], [0, 25, 30, 0]]\n0 3",
                "output": "35",
            },
            {
                "input": "5\n[[0, 1, 4, 0, 0], [1, 0, 2, 5, 0], [4, 2, 0, 3, 0], [0, 5, 3, 0, 1], [0, 0, 0, 1, 0]]\n0 4",
                "output": "7",
            },
        ],
        "edge_cases": [{"input": "2\n[[0, 10], [10, 0]]\n0 1", "output": "10"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq00456789012",
        "problem_description": "Write a Python function to solve the N-Queens problem using backtracking.",
        "input_format": "Input consists of a single integer n representing the size of the board (n x n).",
        "output_format": "Output should be a list of solutions, where each solution is represented by a list of integers where each integer represents the column position of the queen in the corresponding row.",
        "constraints": "1 <= n <= 10.",
        "examples": [
            {"input": "4", "output": "[[1, 3, 0, 2], [2, 0, 3, 1]]"},
            {"input": "1", "output": "[[0]]"},
        ],
        "edge_cases": [{"input": "2", "output": "[]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq00567890123",
        "problem_description": "Write a Python function that calculates the longest common subsequence (LCS) of two strings.",
        "input_format": "Input consists of two strings, s1 and s2, with lengths between 1 and 1000 characters.",
        "output_format": "Output should be an integer representing the length of the longest common subsequence.",
        "constraints": "1 <= len(s1), len(s2) <= 1000.",
        "examples": [
            {"input": "ABCBDAB\nBDCABB", "output": "4"},
            {"input": "AGGTAB\nGXTXAYB", "output": "4"},
        ],
        "edge_cases": [{"input": "A\nA", "output": "1"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq00678901234",
        "problem_description": "Write a Python function to find the median of two sorted arrays.",
        "input_format": "Input consists of two sorted arrays of integers.",
        "output_format": "Output should be a floating-point number representing the median of the two arrays.",
        "constraints": "The length of each array will not exceed 10^4. The arrays will be sorted in ascending order.",
        "examples": [
            {"input": "[1, 3]\n[2]", "output": "2.0"},
            {"input": "[1, 2]\n[3, 4]", "output": "2.5"},
        ],
        "edge_cases": [{"input": "[1, 2, 3, 4]\n[5, 6, 7, 8]", "output": "4.5"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq00789012345",
        "problem_description": "Write a Python function to implement the sliding window technique for finding the maximum sum of a subarray of a given size.",
        "input_format": "Input consists of an array of integers and an integer k representing the size of the subarray.",
        "output_format": "Output should be the maximum sum of any subarray of size k.",
        "constraints": "1 <= len(arr) <= 10^5, 1 <= k <= len(arr).",
        "examples": [
            {"input": "[2, 1, 5, 1, 3, 2]\n3", "output": "9"},
            {"input": "[1, 2, 3, 4, 5]\n2", "output": "9"},
        ],
        "edge_cases": [{"input": "[1, 1, 1, 1, 1]\n3", "output": "3"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq00890123456",
        "problem_description": "Write a Python function to find the minimum number of operations required to convert one string to another using insertions, deletions, and substitutions.",
        "input_format": "Input consists of two strings, s1 and s2, with lengths between 1 and 1000 characters.",
        "output_format": "Output should be the minimum number of operations required to convert s1 to s2.",
        "constraints": "1 <= len(s1), len(s2) <= 1000.",
        "examples": [
            {"input": "kitten\nsitting", "output": "3"},
            {"input": "flaw\nlawn", "output": "4"},
        ],
        "edge_cases": [{"input": "a\nb", "output": "1"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq00901234567",
        "problem_description": "Write a Python function to determine if a given number is a prime number.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be a boolean value, True if n is a prime number, otherwise False.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [
            {"input": "7", "output": "True"},
            {"input": "10", "output": "False"},
        ],
        "edge_cases": [
            {"input": "1", "output": "False"},
            {"input": "2", "output": "True"},
        ],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq01012345678",
        "problem_description": "Write a Python function that finds all the permutations of a given string.",
        "input_format": "Input consists of a string containing only alphabetical characters.",
        "output_format": "Output should be a list of all unique permutations of the string.",
        "constraints": "The length of the string will be at most 9.",
        "examples": [
            {"input": "abc", "output": "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"},
            {"input": "aab", "output": "['aab', 'aba', 'baa']"},
        ],
        "edge_cases": [{"input": "a", "output": "['a']"}],
        "difficulty_level": "Medium",
    },
]


print(
    f"➡ length of problem_solvinge_question_entries: {
      len(problem_solvinge_question_entries)}"
)

# randomly select one feedback entry
selected_psq = random.choice(problem_solvinge_question_entries)

# create the session
session = db_session()

# use the selected entry in PSq_entry
psq_entry = ProblemSolvingQuestion(
    difficulty_level=selected_psq["difficulty_level"],
    problem_description=selected_psq["problem_description"],
    input_format=selected_psq["input_format"],
    output_format=selected_psq["output_format"],
    constraints=selected_psq["constraints"],
    examples=selected_psq["examples"],
    edge_cases=selected_psq["edge_cases"],
)

# retrieve all feedback entries from the database and print them
psq_obj = (
    session.query(ProblemSolvingQuestion)
    .filter(ProblemSolvingQuestion.problem_description == psq_entry.problem_description)
    .all()
)

if not psq_obj:
    session.add(psq_entry)
    session.commit()
    print("\n=====================> PSQ Data added successfully!!!\n")

    print(psq_entry)

else:
    print("\n=====================> This Question is already Added!!!\n")
    for obj in psq_obj:
        print(obj)
