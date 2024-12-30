import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import Feedback, db_session  # noqa: E402

# create the session
session = db_session()

# retrieve all feedback entries from the database and print them
all_feedback = session.query(Feedback).all()

# print a header for the table
print("\n" + "=" * 130)
print(
    f"{'ID':<36} {'Rating':<8} {'Comments':<50} {'Frequency':<12} {'Purpose':<20} {
      'Ease of Use':<15} {'Specific Features':<30} {'Created At':<25}"
)
print("=" * 130)

# loop through all feedback entries and print them in a neat table format
for feedback in all_feedback:
    # convert UUID to string before formatting
    feedback_id_str = str(feedback.id)

    print(
        f"{feedback_id_str:<36} {feedback.rating:<8} {feedback.comments[:47]:<47} {feedback.frequency_of_use:<12} "
        f"{feedback.purpose_of_use[:18]:<20} {feedback.ease_of_use:<15} {feedback.specific_features[:27]:<30} {str(feedback.created_at):<25}"
    )

print("=" * 130)

print("-" * 130)
print(f"➡ Total Data Count: {len(all_feedback)}")
print("-" * 130)
