import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent)
sys.path.append(__path)

from app.services import question_service_obj  # noqa: E402

questions_payload = dict(
    num_questions=10,
    difficulty_level="hard",
    programming_language="python",
    topics=["loops", "functions"],
)
service_instance = question_service_obj(questions_payload)
print("➡ service_instance:", service_instance)
