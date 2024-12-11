import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


from services import question_service_obj

questions_payload = dict(
    num_questions=1,
    difficulty_level="easy",
    programming_language="python",
    topics=["loops", "functions"],
)
service_instance = question_service_obj(**questions_payload)
print("➡ service_instance:", service_instance)
