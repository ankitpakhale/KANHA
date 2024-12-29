import sys
from pathlib import Path

# Add the `app` directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from prompts import prompt_factory

question_generation_obj = prompt_factory.create_prompt(
    prompt_type="question_generation",
    num_questions=5,  # optional
    difficulty_level="easy",
    programming_language="python",
    topics="all",
)

question_generation_system_prompt = question_generation_obj.get_system_prompt()
print("➡ Question Generation System Prompt:", question_generation_system_prompt)

question_generation_user_prompt = question_generation_obj.get_user_prompt()
print("➡ Question Generation User Prompt:", question_generation_user_prompt)
