import sys
from pathlib import Path

# add the src directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(__path)

from dao import Feedback, db_session  # noqa: E402
import random  # noqa: E402

# list of feedback entries
feedback_entries = [
    {
        "rating": 10,
        "comments": "Incredible tool for productivity!",
        "frequency_of_use": "Weekly",
        "purpose_of_use": "Personal",
        "ease_of_use": "Easy",
        "specific_features": "Task Management",
    },
    {
        "rating": 9,
        "comments": "Great user interface and functionality.",
        "frequency_of_use": "Daily",
        "purpose_of_use": "Work",
        "ease_of_use": "Very Easy",
        "specific_features": "Reporting",
    },
    {
        "rating": 10,
        "comments": "Best app I've used in a while!",
        "frequency_of_use": "Weekly",
        "purpose_of_use": "Study",
        "ease_of_use": "Very Easy",
        "specific_features": "Notes",
    },
    {
        "rating": 8,
        "comments": "Very useful for tracking projects.",
        "frequency_of_use": "Daily",
        "purpose_of_use": "Work",
        "ease_of_use": "Easy",
        "specific_features": "Project Management",
    },
    {
        "rating": 10,
        "comments": "Fantastic design and excellent features.",
        "frequency_of_use": "Daily",
        "purpose_of_use": "Work",
        "ease_of_use": "Very Easy",
        "specific_features": "Reporting",
    },
    {
        "rating": 9,
        "comments": "App works seamlessly and is very efficient.",
        "frequency_of_use": "Weekly",
        "purpose_of_use": "Work",
        "ease_of_use": "Easy",
        "specific_features": "Dashboard",
    },
    {
        "rating": 10,
        "comments": "User-friendly and intuitive. Perfect for my needs!",
        "frequency_of_use": "Daily",
        "purpose_of_use": "Personal",
        "ease_of_use": "Very Easy",
        "specific_features": "Task Management",
    },
    {
        "rating": 9,
        "comments": "I love how customizable this app is.",
        "frequency_of_use": "Weekly",
        "purpose_of_use": "Personal",
        "ease_of_use": "Easy",
        "specific_features": "Customization",
    },
    {
        "rating": 10,
        "comments": "Everything works perfectly, no bugs.",
        "frequency_of_use": "Daily",
        "purpose_of_use": "Work",
        "ease_of_use": "Very Easy",
        "specific_features": "Analytics",
    },
    {
        "rating": 8,
        "comments": "A solid app with great support.",
        "frequency_of_use": "Weekly",
        "purpose_of_use": "Work",
        "ease_of_use": "Easy",
        "specific_features": "Customer Support",
    },
]

# randomly select one feedback entry
selected_feedback = random.choice(feedback_entries)

# create the session
session = db_session()

# use the selected entry in feedback_entry
feedback_entry = Feedback(
    rating=selected_feedback["rating"],
    # comments=selected_feedback["comments"],
    # frequency_of_use=selected_feedback["frequency_of_use"],
    # purpose_of_use=selected_feedback["purpose_of_use"],
    # ease_of_use=selected_feedback["ease_of_use"],
    # specific_features=selected_feedback["specific_features"],
)

session.add(feedback_entry)
session.commit()
print("Feedback Data added successfully!!!")

print(feedback_entry)
