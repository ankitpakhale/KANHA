import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import ProblemSolvingQuestion, db_session  # noqa: E402

# list of feedback entries
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
    {
        "q_id": "psq01123456789",
        "problem_description": "Write a Python function that checks whether two strings are anagrams of each other.",
        "input_format": "Input consists of two strings, s1 and s2.",
        "output_format": "Output should be a boolean value, True if the strings are anagrams, otherwise False.",
        "constraints": "1 <= len(s1), len(s2) <= 1000.",
        "examples": [
            {"input": "listen\nsilent", "output": "True"},
            {"input": "hello\nworld", "output": "False"},
        ],
        "edge_cases": [{"input": "a\na", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq01234567890",
        "problem_description": "Write a Python function to find the intersection of two arrays.",
        "input_format": "Input consists of two lists of integers, arr1 and arr2.",
        "output_format": "Output should be a list of integers that are common in both arrays.",
        "constraints": "1 <= len(arr1), len(arr2) <= 10^4.",
        "examples": [
            {"input": "[1, 2, 2, 1]\n[2, 2]", "output": "[2, 2]"},
            {"input": "[4, 9, 5]\n[9, 4, 9, 8, 4]", "output": "[4, 9]"},
        ],
        "edge_cases": [{"input": "[1, 2, 3]\n[4, 5, 6]", "output": "[]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq01345678901",
        "problem_description": "Write a Python function to find the longest substring without repeating characters.",
        "input_format": "Input consists of a string s.",
        "output_format": "Output should be an integer representing the length of the longest substring without repeating characters.",
        "constraints": "1 <= len(s) <= 10^5.",
        "examples": [
            {"input": "abcabcbb", "output": "3"},
            {"input": "bbbbb", "output": "1"},
        ],
        "edge_cases": [{"input": "pwwkew", "output": "3"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq01456789012",
        "problem_description": "Write a Python function to implement the binary search algorithm on a sorted array.",
        "input_format": "Input consists of a sorted array of integers and a target integer.",
        "output_format": "Output should be the index of the target integer if it exists in the array, otherwise -1.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[1, 2, 3, 4, 5, 6, 7]\n4", "output": "3"},
            {"input": "[1, 2, 3, 4, 5, 6]\n0", "output": "-1"},
        ],
        "edge_cases": [{"input": "[1, 2, 3, 4]\n5", "output": "-1"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq01567890123",
        "problem_description": "Write a Python function to reverse a linked list.",
        "input_format": "Input consists of the head node of a singly linked list.",
        "output_format": "Output should be the head node of the reversed linked list.",
        "constraints": "1 <= len(list) <= 10^5.",
        "examples": [
            {"input": "[1, 2, 3, 4, 5]", "output": "[5, 4, 3, 2, 1]"},
            {"input": "[1, 2]", "output": "[2, 1]"},
        ],
        "edge_cases": [{"input": "[1]", "output": "[1]"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq01678901234",
        "problem_description": "Write a Python function to find the Kth largest element in an array.",
        "input_format": "Input consists of an array of integers and an integer k.",
        "output_format": "Output should be the Kth largest element in the array.",
        "constraints": "1 <= len(arr) <= 10^5, 1 <= k <= len(arr).",
        "examples": [
            {"input": "[3, 2, 1, 5, 6, 4]\n2", "output": "5"},
            {"input": "[3, 2, 3, 1, 2, 4, 5, 5, 6]\n4", "output": "4"},
        ],
        "edge_cases": [{"input": "[1, 2, 3]\n1", "output": "3"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq01789012345",
        "problem_description": "Write a Python function to implement a depth-first search (DFS) on a graph.",
        "input_format": "Input consists of an adjacency list of a graph and a start node.",
        "output_format": "Output should be a list of nodes visited in the DFS order.",
        "constraints": "The graph will contain between 1 and 1000 nodes.",
        "examples": [
            {
                "input": "{0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}\n0",
                "output": "[0, 1, 3, 2, 4]",
            },
            {"input": "{0: [1, 2], 1: [3], 2: [], 3: []}\n0", "output": "[0, 1, 3, 2]"},
        ],
        "edge_cases": [{"input": "{0: []}\n0", "output": "[0]"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq01890123456",
        "problem_description": "Write a Python function to find the longest increasing subsequence in an array.",
        "input_format": "Input consists of an array of integers.",
        "output_format": "Output should be the length of the longest increasing subsequence.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[10, 9, 2, 5, 3, 7, 101, 18]", "output": "4"},
            {"input": "[3, 2, 6, 4, 5, 1]", "output": "3"},
        ],
        "edge_cases": [{"input": "[1, 2, 3, 4, 5]", "output": "5"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq01901234567",
        "problem_description": "Write a Python function to check if a given binary tree is balanced.",
        "input_format": "Input consists of the root node of a binary tree.",
        "output_format": "Output should be True if the binary tree is balanced, otherwise False.",
        "constraints": "1 <= number of nodes <= 10^4.",
        "examples": [
            {"input": "[3, 9, 20, null, null, 15, 7]", "output": "True"},
            {"input": "[1, 2, 2, 3, 3, null, null, 4, 4]", "output": "False"},
        ],
        "edge_cases": [{"input": "[1]", "output": "True"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq02012345678",
        "problem_description": "Write a Python function to rotate an array to the right by k steps.",
        "input_format": "Input consists of an array of integers and an integer k representing the number of steps to rotate.",
        "output_format": "Output should be the rotated array.",
        "constraints": "1 <= len(arr) <= 10^5, 1 <= k <= len(arr).",
        "examples": [
            {"input": "[1, 2, 3, 4, 5, 6, 7]\n3", "output": "[5, 6, 7, 1, 2, 3, 4]"},
            {"input": "[1, 2, 3, 4, 5]\n2", "output": "[4, 5, 1, 2, 3]"},
        ],
        "edge_cases": [{"input": "[1, 2, 3]\n0", "output": "[1, 2, 3]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02123456789",
        "problem_description": "Write a Python function to find the unique elements in an array that appear only once.",
        "input_format": "Input consists of an array of integers.",
        "output_format": "Output should be a list of unique integers that appear only once in the array.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[4, 3, 2, 7, 8, 3, 2, 1]", "output": "[4, 7, 8, 1]"},
            {"input": "[1, 2, 2, 1, 3]", "output": "[3]"},
        ],
        "edge_cases": [{"input": "[10, 10, 10, 10]", "output": "[]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02234567890",
        "problem_description": "Write a Python function to check if a number is a perfect square.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be True if n is a perfect square, otherwise False.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [
            {"input": "16", "output": "True"},
            {"input": "14", "output": "False"},
        ],
        "edge_cases": [{"input": "1", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02345678901",
        "problem_description": "Write a Python function to merge two sorted arrays into a single sorted array.",
        "input_format": "Input consists of two sorted arrays of integers.",
        "output_format": "Output should be a single sorted array containing all elements from both arrays.",
        "constraints": "1 <= len(arr1), len(arr2) <= 10^4.",
        "examples": [
            {
                "input": "[1, 3, 5, 7]\n[2, 4, 6, 8]",
                "output": "[1, 2, 3, 4, 5, 6, 7, 8]",
            },
            {"input": "[1, 2, 3]\n[0, 4, 5]", "output": "[0, 1, 2, 3, 4, 5]"},
        ],
        "edge_cases": [{"input": "[1, 3, 5]\n[]", "output": "[1, 3, 5]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02456789012",
        "problem_description": "Write a Python function to find the longest palindrome in a string.",
        "input_format": "Input consists of a string s.",
        "output_format": "Output should be the longest palindrome substring in s.",
        "constraints": "1 <= len(s) <= 10^5.",
        "examples": [
            {"input": "babad", "output": "bab"},
            {"input": "cbbd", "output": "bb"},
        ],
        "edge_cases": [{"input": "a", "output": "a"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq02567890123",
        "problem_description": "Write a Python function to find the sum of all prime numbers up to a given number n.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be the sum of all prime numbers less than or equal to n.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [{"input": "10", "output": "17"}, {"input": "5", "output": "10"}],
        "edge_cases": [{"input": "1", "output": "0"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02678901234",
        "problem_description": "Write a Python function to generate all possible combinations of a given list of numbers.",
        "input_format": "Input consists of a list of integers.",
        "output_format": "Output should be a list of lists, where each list is a combination of elements.",
        "constraints": "1 <= len(arr) <= 12.",
        "examples": [
            {
                "input": "[1, 2, 3]",
                "output": "[[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]",
            },
            {"input": "[0, 1]", "output": "[[0], [1], [0, 1]]"},
        ],
        "edge_cases": [{"input": "[1]", "output": "[[1]]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02789012345",
        "problem_description": "Write a Python function to check if two strings are isomorphic.",
        "input_format": "Input consists of two strings s1 and s2.",
        "output_format": "Output should be True if the strings are isomorphic, otherwise False.",
        "constraints": "1 <= len(s1), len(s2) <= 10^5.",
        "examples": [
            {"input": "egg\nadd", "output": "True"},
            {"input": "foo\nbar", "output": "False"},
        ],
        "edge_cases": [{"input": "a\na", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq02890123456",
        "problem_description": "Write a Python function to implement the merge sort algorithm.",
        "input_format": "Input consists of an array of integers.",
        "output_format": "Output should be the sorted array.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {
                "input": "[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]",
                "output": "[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]",
            },
            {"input": "[8, 7, 6, 5, 4, 3, 2, 1]", "output": "[1, 2, 3, 4, 5, 6, 7, 8]"},
        ],
        "edge_cases": [{"input": "[1, 2, 3]", "output": "[1, 2, 3]"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq02901234567",
        "problem_description": "Write a Python function to determine if a string has all unique characters.",
        "input_format": "Input consists of a string s.",
        "output_format": "Output should be True if the string has all unique characters, otherwise False.",
        "constraints": "1 <= len(s) <= 10^5.",
        "examples": [
            {"input": "abcdef", "output": "True"},
            {"input": "aabbcc", "output": "False"},
        ],
        "edge_cases": [{"input": "a", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq03012345678",
        "problem_description": "Write a Python function to find the longest increasing subsequence in an array.",
        "input_format": "Input consists of an array of integers.",
        "output_format": "Output should be an integer representing the length of the longest increasing subsequence.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[10, 9, 2, 5, 3, 7, 101, 18]", "output": "4"},
            {"input": "[0, 1, 0, 3, 2, 3]", "output": "4"},
        ],
        "edge_cases": [{"input": "[1, 2, 3, 4, 5]", "output": "5"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq03123456789",
        "problem_description": "Write a Python function to find the kth smallest element in an unsorted array.",
        "input_format": "Input consists of an array of integers and an integer k.",
        "output_format": "Output should be the kth smallest element in the array.",
        "constraints": "1 <= len(arr) <= 10^5, 1 <= k <= len(arr).",
        "examples": [
            {"input": "[7, 10, 4, 3, 20, 15]\n4", "output": "10"},
            {"input": "[12, 3, 5, 7, 19]\n2", "output": "5"},
        ],
        "edge_cases": [{"input": "[5, 5, 5, 5, 5]\n1", "output": "5"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq03234567890",
        "problem_description": "Write a Python function to generate Pascal's Triangle up to the nth row.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be a list of lists representing the first n rows of Pascal's Triangle.",
        "constraints": "1 <= n <= 30.",
        "examples": [
            {
                "input": "5",
                "output": "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]",
            },
            {"input": "3", "output": "[[1], [1, 1], [1, 2, 1]]"},
        ],
        "edge_cases": [{"input": "1", "output": "[[1]]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq03345678901",
        "problem_description": "Write a Python function to find all the prime factors of a given number n.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be a list of prime factors of n.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [
            {"input": "28", "output": "[2, 2, 7]"},
            {"input": "12", "output": "[2, 2, 3]"},
        ],
        "edge_cases": [{"input": "1", "output": "[]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq03456789012",
        "problem_description": "Write a Python function to find the maximum product subarray in a given array of integers.",
        "input_format": "Input consists of an array of integers.",
        "output_format": "Output should be the maximum product of any subarray.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[2, 3, -2, 4]", "output": "6"},
            {"input": "[-2, 0, -1]", "output": "0"},
        ],
        "edge_cases": [{"input": "[-2, -3, 0, -2, -40]", "output": "240"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq03567890123",
        "problem_description": "Write a Python function to find the maximum sum of a subarray of size k.",
        "input_format": "Input consists of an array of integers and an integer k.",
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
        "q_id": "psq03678901234",
        "problem_description": "Write a Python function to check if a number is a power of two.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be True if n is a power of two, otherwise False.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [
            {"input": "16", "output": "True"},
            {"input": "18", "output": "False"},
        ],
        "edge_cases": [{"input": "1", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq03789012345",
        "problem_description": "Write a Python function to implement binary search on a sorted array.",
        "input_format": "Input consists of a sorted array of integers and an integer target.",
        "output_format": "Output should be the index of the target in the array, or -1 if the target is not found.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[1, 3, 5, 7, 9, 11]\n5", "output": "2"},
            {"input": "[1, 2, 3, 4, 5]\n6", "output": "-1"},
        ],
        "edge_cases": [{"input": "[1, 3, 5, 7]\n3", "output": "1"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq03890123456",
        "problem_description": "Write a Python function to find the longest substring without repeating characters.",
        "input_format": "Input consists of a string s.",
        "output_format": "Output should be the length of the longest substring without repeating characters.",
        "constraints": "1 <= len(s) <= 10^5.",
        "examples": [
            {"input": "abcabcbb", "output": "3"},
            {"input": "bbbbb", "output": "1"},
        ],
        "edge_cases": [{"input": "pwwkew", "output": "3"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq04012345678",
        "problem_description": "Write a Python function to implement a basic calculator that supports addition, subtraction, multiplication, and division.",
        "input_format": "Input consists of a string containing a mathematical expression.",
        "output_format": "Output should be the result of the evaluation of the expression.",
        "constraints": "The expression will only contain integers and operators (+, -, *, /).",
        "examples": [
            {"input": "3+2*2", "output": "7"},
            {"input": "3/2", "output": "1"},
        ],
        "edge_cases": [{"input": "3+5/2", "output": "5"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq04123456789",
        "problem_description": "Write a Python function to check if two strings are anagrams of each other.",
        "input_format": "Input consists of two strings, s1 and s2.",
        "output_format": "Output should be True if the strings are anagrams, otherwise False.",
        "constraints": "1 <= len(s1), len(s2) <= 10^5.",
        "examples": [
            {"input": "anagram\nnagaram", "output": "True"},
            {"input": "rat\ncar", "output": "False"},
        ],
        "edge_cases": [{"input": "listen\nsilent", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq04234567890",
        "problem_description": "Write a Python function to find the missing number in a list of consecutive numbers.",
        "input_format": "Input consists of a list of n-1 integers from 1 to n.",
        "output_format": "Output should be the missing number.",
        "constraints": "The length of the list will be at most 10^5.",
        "examples": [
            {"input": "[1, 2, 4, 5, 6]", "output": "3"},
            {"input": "[2, 3, 4, 5]", "output": "1"},
        ],
        "edge_cases": [{"input": "[2]", "output": "1"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq04345678901",
        "problem_description": "Write a Python function to count the number of words in a sentence, ignoring punctuation and spaces.",
        "input_format": "Input consists of a string s containing words and punctuation.",
        "output_format": "Output should be an integer representing the word count.",
        "constraints": "The length of the string will be at most 10^5.",
        "examples": [
            {"input": "Hello, world! How are you?", "output": "5"},
            {"input": "Python is great.", "output": "3"},
        ],
        "edge_cases": [{"input": "   ", "output": "0"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq04456789012",
        "problem_description": "Write a Python function to remove duplicates from a sorted array.",
        "input_format": "Input consists of a sorted array of integers.",
        "output_format": "Output should be the array after removing duplicates.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[1, 1, 2]", "output": "[1, 2]"},
            {"input": "[0, 0, 1, 1, 2, 2, 3]", "output": "[0, 1, 2, 3]"},
        ],
        "edge_cases": [{"input": "[1, 1, 1]", "output": "[1]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq04567890123",
        "problem_description": "Write a Python function to reverse a linked list.",
        "input_format": "Input consists of the head node of a linked list.",
        "output_format": "Output should be the head node of the reversed linked list.",
        "constraints": "The linked list will contain at least one node.",
        "examples": [
            {"input": "[1, 2, 3, 4, 5]", "output": "[5, 4, 3, 2, 1]"},
            {"input": "[1]", "output": "[1]"},
        ],
        "edge_cases": [{"input": "[2, 1]", "output": "[1, 2]"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq04678901234",
        "problem_description": "Write a Python function to implement a stack using two queues.",
        "input_format": "Input consists of a series of operations to perform on the stack.",
        "output_format": "Output should be the result of the operations performed on the stack.",
        "constraints": "1 <= len(operations) <= 10^4.",
        "examples": [
            {"input": "push(1), push(2), pop()", "output": "2"},
            {"input": "push(3), push(4), pop(), pop()", "output": "4, 3"},
        ],
        "edge_cases": [{"input": "pop()", "output": "Error: Stack is empty"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq04789012345",
        "problem_description": "Write a Python function to implement depth-first search (DFS) on a graph.",
        "input_format": "Input consists of a graph represented as an adjacency list and a start node.",
        "output_format": "Output should be a list of nodes visited in DFS order.",
        "constraints": "1 <= n <= 100.",
        "examples": [
            {
                "input": "adjacency_list = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}, start = 0",
                "output": "[0, 1, 3, 2]",
            },
            {
                "input": "adjacency_list = {0: [1], 1: [0]}, start = 0",
                "output": "[0, 1]",
            },
        ],
        "edge_cases": [
            {"input": "adjacency_list = {0: []}, start = 0", "output": "[0]"}
        ],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq04890123456",
        "problem_description": "Write a Python function to implement breadth-first search (BFS) on a graph.",
        "input_format": "Input consists of a graph represented as an adjacency list and a start node.",
        "output_format": "Output should be a list of nodes visited in BFS order.",
        "constraints": "1 <= n <= 100.",
        "examples": [
            {
                "input": "adjacency_list = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}, start = 0",
                "output": "[0, 1, 2, 3]",
            },
            {
                "input": "adjacency_list = {0: [1], 1: [0]}, start = 0",
                "output": "[0, 1]",
            },
        ],
        "edge_cases": [
            {"input": "adjacency_list = {0: []}, start = 0", "output": "[0]"}
        ],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq04901234567",
        "problem_description": "Write a Python function to perform matrix multiplication.",
        "input_format": "Input consists of two matrices A and B where the number of columns of A is equal to the number of rows of B.",
        "output_format": "Output should be the resultant matrix after multiplication.",
        "constraints": "1 <= len(A), len(B) <= 100.",
        "examples": [
            {
                "input": "[[1, 2], [3, 4]]\n[[5, 6], [7, 8]]",
                "output": "[[19, 22], [43, 50]]",
            },
            {
                "input": "[[1, 0], [0, 1]]\n[[1, 1], [1, 1]]",
                "output": "[[1, 1], [1, 1]]",
            },
        ],
        "edge_cases": [{"input": "[[1]]\n[[1]]", "output": "[[1]]"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq05012345678",
        "problem_description": "Write a Python function to solve the knapsack problem using dynamic programming.",
        "input_format": "Input consists of an array of values and weights of items, and the maximum capacity of the knapsack.",
        "output_format": "Output should be the maximum value that can be obtained.",
        "constraints": "1 <= len(weights) <= 100, 1 <= capacity <= 100.",
        "examples": [
            {"input": "[60, 100, 120]\n[10, 20, 30]\n50", "output": "220"},
            {"input": "[60, 50, 70]\n[10, 20, 30]\n50", "output": "120"},
        ],
        "edge_cases": [{"input": "[10]\n[1]\n10", "output": "10"}],
        "difficulty_level": "High",
    },
    {
        "q_id": "psq05123456789",
        "problem_description": "Write a Python function to check if a given number is a perfect square.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be a boolean value, True if n is a perfect square, otherwise False.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [
            {"input": "16", "output": "True"},
            {"input": "14", "output": "False"},
        ],
        "edge_cases": [{"input": "1", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05234567890",
        "problem_description": "Write a Python function to merge two sorted arrays into one sorted array.",
        "input_format": "Input consists of two sorted arrays of integers.",
        "output_format": "Output should be a sorted array containing all elements of both input arrays.",
        "constraints": "1 <= len(arr1), len(arr2) <= 10^4.",
        "examples": [
            {"input": "[1, 3, 5]\n[2, 4, 6]", "output": "[1, 2, 3, 4, 5, 6]"},
            {"input": "[0, 2, 4]\n[1, 3, 5]", "output": "[0, 1, 2, 3, 4, 5]"},
        ],
        "edge_cases": [{"input": "[1, 2, 3]\n[]", "output": "[1, 2, 3]"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05345678901",
        "problem_description": "Write a Python function to find the first non-repeating character in a string.",
        "input_format": "Input consists of a string s.",
        "output_format": "Output should be the first non-repeating character in the string, or None if all characters repeat.",
        "constraints": "1 <= len(s) <= 10^5.",
        "examples": [
            {"input": "swiss", "output": "w"},
            {"input": "aabbcc", "output": "None"},
        ],
        "edge_cases": [{"input": "abcd", "output": "a"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05456789012",
        "problem_description": "Write a Python function to find the nth Fibonacci number using dynamic programming.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be the nth Fibonacci number.",
        "constraints": "1 <= n <= 10^6.",
        "examples": [{"input": "5", "output": "5"}, {"input": "10", "output": "55"}],
        "edge_cases": [{"input": "1", "output": "1"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05567890123",
        "problem_description": "Write a Python function to convert a Roman numeral to an integer.",
        "input_format": "Input consists of a string s representing the Roman numeral.",
        "output_format": "Output should be the integer value of the Roman numeral.",
        "constraints": "1 <= len(s) <= 15.",
        "examples": [{"input": "III", "output": "3"}, {"input": "IX", "output": "9"}],
        "edge_cases": [{"input": "M", "output": "1000"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05678901234",
        "problem_description": "Write a Python function to find the sum of the digits of a given number.",
        "input_format": "Input consists of a single integer n.",
        "output_format": "Output should be the sum of the digits of n.",
        "constraints": "1 <= n <= 10^9.",
        "examples": [
            {"input": "12345", "output": "15"},
            {"input": "9876", "output": "30"},
        ],
        "edge_cases": [{"input": "0", "output": "0"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05789012345",
        "problem_description": "Write a Python function to check if a given string is a valid email address.",
        "input_format": "Input consists of a string s.",
        "output_format": "Output should be True if the string is a valid email address, otherwise False.",
        "constraints": "1 <= len(s) <= 100.",
        "examples": [
            {"input": "example@domain.com", "output": "True"},
            {"input": "invalid-email.com", "output": "False"},
        ],
        "edge_cases": [{"input": "user@sub.domain.com", "output": "True"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05890123456",
        "problem_description": "Write a Python function to find the second largest number in a list of integers.",
        "input_format": "Input consists of a list of integers.",
        "output_format": "Output should be the second largest number in the list.",
        "constraints": "2 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[1, 2, 3, 4, 5]", "output": "4"},
            {"input": "[5, 5, 5, 5]", "output": "5"},
        ],
        "edge_cases": [{"input": "[1, 2]", "output": "1"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq05901234567",
        "problem_description": "Write a Python function to find the most frequent element in an array.",
        "input_format": "Input consists of an array of integers.",
        "output_format": "Output should be the most frequent element. If there is a tie, return the smallest element.",
        "constraints": "1 <= len(arr) <= 10^5.",
        "examples": [
            {"input": "[1, 2, 2, 3, 3, 3, 4]", "output": "3"},
            {"input": "[1, 1, 2, 2, 2, 3]", "output": "2"},
        ],
        "edge_cases": [{"input": "[1]", "output": "1"}],
        "difficulty_level": "Medium",
    },
    {
        "q_id": "psq06012345678",
        "problem_description": "Write a Python function to rotate an array to the right by k steps.",
        "input_format": "Input consists of an array of integers and an integer k.",
        "output_format": "Output should be the array after rotating it to the right by k steps.",
        "constraints": "1 <= len(arr) <= 10^5, 0 <= k < len(arr).",
        "examples": [
            {"input": "[1, 2, 3, 4, 5], 2", "output": "[4, 5, 1, 2, 3]"},
            {"input": "[1, 2, 3, 4], 1", "output": "[4, 1, 2, 3]"},
        ],
        "edge_cases": [{"input": "[1, 2, 3], 0", "output": "[1, 2, 3]"}],
        "difficulty_level": "Medium",
    },
]


print(
    f"➡ length of problem_solvinge_question_entries: {len(problem_solvinge_question_entries)}"
)

# create the session
session = db_session()

duplicate_questions = []

for selected_psq in problem_solvinge_question_entries:
    # use the selected entry in psq_entry
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
        .filter(
            ProblemSolvingQuestion.problem_description == psq_entry.problem_description
        )
        .all()
    )

    if not psq_obj:
        session.add(psq_entry)
        session.commit()
        print("=====================> PSQ Data added successfully!!!")
    else:
        print("=====================> This Question is already Added!!!")
        for obj in psq_obj:
            duplicate_questions.append(obj.problem_description)

print(f"=====================> duplicate_questions: {duplicate_questions}")