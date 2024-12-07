import sys
import os

# add the root directory of your project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from prompt_manager import prompt_factory

answer_evaluation_obj = prompt_factory.create_prompt(
    prompt_type="answer_evaluation",
    user_code={
        "q_type": "MCQ",
        "question": "What is the correct way to initialize an empty array in Python?",
        "options": ["array = []", "array = {}", "array = ()", "array = None"],
        "correct_answer": "array = []",
    },
)

answer_system_prompt = answer_evaluation_obj.get_system_prompt()
print("➡ >>>>>>>>>>>> answer_system_prompt:", answer_system_prompt)

answer_user_prompt = answer_evaluation_obj.get_user_prompt()
print("➡ >>>>>>>>>>>> answer_user_prompt:", answer_user_prompt)
