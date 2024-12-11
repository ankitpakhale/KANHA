import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


from services import evaluation_service_obj

answer_payload = dict(
    user_code=[
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
        }
    ]
)
service_instance = evaluation_service_obj(**answer_payload)
print("➡ service_instance:", service_instance)
