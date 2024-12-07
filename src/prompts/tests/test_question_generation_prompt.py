import sys
import os

# add the root directory of your project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from prompt_manager import prompt_factory

question_generation_obj = prompt_factory.create_prompt(
    prompt_type="question_generation",
    num_questions=5,  # optional
    difficulty_level="easy",
    programming_language="python",
    topics="all",
)

question_system_prompt = question_generation_obj.get_system_prompt()
print("➡ >>>>>>>>>>>> question_system_prompt:", question_system_prompt)

question_user_prompt = question_generation_obj.get_user_prompt()
print("➡ >>>>>>>>>>>> question_user_prompt:", question_user_prompt)
