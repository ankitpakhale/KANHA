import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import ProblemSolvingQuestion, db_session  # noqa: E402

# create the session
session = db_session()

# retrieve all psq entries from the database and print them
all_psq = session.query(ProblemSolvingQuestion).all()

# loop through all psq entries and print them in a neat table format
for psq in all_psq:
    # convert UUID to string before formatting
    print(" ======== ======== ======== ======== ======== ======== ======== ======== ")
    print(f"➡ id: {psq.id}")
    print(f"➡ difficulty_level: {psq.difficulty_level}")
    print(f"➡ problem_description: {psq.problem_description}")
    print(f"➡ input_format: {psq.input_format}")
    print(f"➡ output_format: {psq.output_format}")
    print(f"➡ constraints: {psq.constraints}")
    print(f"➡ examples: {psq.examples}")
    print(f"➡ edge_cases: {psq.edge_cases}")
    print(" ======== ======== ======== ======== ======== ======== ======== ======== ")

print("-" * 130)
print(f"➡ Total Data Count: {len(all_psq)}")
print("-" * 130)
