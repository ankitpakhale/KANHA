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

    # safely handle possible None values by using a conditional (ternary) expression
    purpose_of_use = feedback.purpose_of_use[:18] if feedback.purpose_of_use else ""
    ease_of_use = feedback.ease_of_use[:15] if feedback.ease_of_use else ""
    specific_features = (
        feedback.specific_features[:27] if feedback.specific_features else ""
    )

    # format and print the feedback entry
    print(
        f"{feedback_id_str:<36} {feedback.rating:<8} {
            feedback.comments[:47]:<47} {feedback.frequency_of_use:<12} "
        f"{purpose_of_use:<20} {ease_of_use:<15} {
            specific_features:<30} {str(feedback.created_at):<25}"
    )

print("=" * 130)

print("-" * 130)
print(f"➡ Total Data Count: {len(all_feedback)}")
print("-" * 130)
