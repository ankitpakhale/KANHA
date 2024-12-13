import sys
from pathlib import Path

# Add the `src` directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from prompts import prompt_factory
from utils import logger

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
logger.debug("➡ >>>>>>>>>>>> answer_system_prompt:", answer_system_prompt)

answer_user_prompt = answer_evaluation_obj.get_user_prompt()
logger.debug("➡ >>>>>>>>>>>> answer_user_prompt:", answer_user_prompt)
