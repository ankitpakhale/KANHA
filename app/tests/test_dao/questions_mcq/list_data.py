import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import MultipleChoiceQuestion, db_session  # noqa: E402

# create the session
session = db_session()

# retrieve all mcq entries from the database and print them
all_mcq = session.query(MultipleChoiceQuestion).all()

# loop through all mcq entries and print them in a neat table format
for mcq in all_mcq:
    # convert UUID to string before formatting
    print(" ======== ======== ======== ======== ======== ======== ======== ======== ")
    print(f"➡ id: {mcq.id}")
    print(f"➡ difficulty_level: {mcq.difficulty_level}")
    print(f"➡ question: {mcq.question}")
    print(f"➡ option_1: {mcq.option_1}")
    print(f"➡ option_2: {mcq.option_2}")
    print(f"➡ option_3: {mcq.option_3}")
    print(f"➡ option_4: {mcq.option_4}")
    print(f"➡ correct_answer: {mcq.correct_answer}")
    print(" ======== ======== ======== ======== ======== ======== ======== ======== ")

print("-" * 130)
print(f"➡ Total Data Count: {len(all_mcq)}")
print("-" * 130)
