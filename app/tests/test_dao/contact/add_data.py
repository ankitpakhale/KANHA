import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import Contact, db_session  # noqa: E402
import random  # noqa: E402

# list of contact entries
contact_entries = [
    {
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "subject": "Inquiry",
        "message": "I would like more information about your services.",
    },
    {
        "full_name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "987-654-3210",
        "subject": "Feedback",
        "message": "Great website, but I think it could use some improvements.",
    },
    {
        "full_name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "phone": "555-123-4567",
        "subject": "Support Request",
        "message": "Having trouble logging in to my account.",
    },
    {
        "full_name": "Bob Brown",
        "email": "bob.brown@example.com",
        "phone": "555-987-6543",
        "subject": "Complaint",
        "message": "The recent update caused some issues with the app functionality.",
    },
    {
        "full_name": "Charlie Wilson",
        "email": "charlie.wilson@example.com",
        "phone": "555-456-7890",
        "subject": "General Inquiry",
        "message": "Can you provide more details on your pricing structure?",
    },
    {
        "full_name": "David Lee",
        "email": "david.lee@example.com",
        "phone": "555-654-3210",
        "subject": "Appointment Request",
        "message": "Would like to schedule a meeting with your team.",
    },
    {
        "full_name": "Eve Adams",
        "email": "eve.adams@example.com",
        "phone": "555-321-4321",
        "subject": "Partnership Inquiry",
        "message": "Interested in discussing a potential partnership.",
    },
    {
        "full_name": "Frank Miller",
        "email": "frank.miller@example.com",
        "phone": "555-432-1234",
        "subject": "Job Application",
        "message": "I am applying for the developer position listed on your website.",
    },
    {
        "full_name": "Grace Davis",
        "email": "grace.davis@example.com",
        "phone": "555-876-5432",
        "subject": "Customer Feedback",
        "message": "The product I received was great, but the delivery was delayed.",
    },
    {
        "full_name": "Hank Wilson",
        "email": "hank.wilson@example.com",
        "phone": "555-765-4321",
        "subject": "Event Inquiry",
        "message": "I am interested in attending your upcoming conference. Can you send me details?",
    },
]


# randomly select one contact entry
selected_contact = random.choice(contact_entries)

# create the session
session = db_session()

# use the selected entry in contact_entry
contact_entry = Contact(
    full_name=selected_contact["full_name"],
    email=selected_contact["email"],
    phone=selected_contact["phone"],
    subject=selected_contact["subject"],
    message=selected_contact["message"],
)


session.add(contact_entry)
session.commit()
print("\n=====================> Contact Data added successfully!!!\n")

print(contact_entry)
