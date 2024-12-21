import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


from src.dao import Feedback, db_session

session = db_session()
feedback_entry = Feedback(
    rating=10,
    comments="Great app!",
    frequency_of_use="Daily",
    purpose_of_use="Work",
    ease_of_use="Very Easy",
    specific_features="Reporting",
)
session.add(feedback_entry)
session.commit()
print("Data added successfully!!!")
