import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import Contact, db_session  # noqa: E402

# create the session
session = db_session()

# retrieve all contact entries from the database and print them
all_contact = session.query(Contact).all()

# print a header for the table
print("\n" + "=" * 130)
print(
    f"{'ID':<36} {'Full Name':<30} {'Email':<40} {'Phone':<20} {
        'Subject':<30} {'Message':<50} {'Created At':<25}"
)
print("=" * 130)

# loop through all contact entries and print them in a neat table format
for contact in all_contact:
    # convert UUID to string before formatting
    contact_id_str = str(contact.id)

    # safely handle possible None values by using a conditional (ternary) expression
    full_name = contact.full_name[:28] if contact.full_name else ""
    email = contact.email[:38] if contact.email else ""
    phone = contact.phone[:18] if contact.phone else ""
    subject = contact.subject[:28] if contact.subject else ""
    message = contact.message[:48] if contact.message else ""

    # format and print the contact entry
    print(
        f"{contact_id_str:<36} {full_name:<30} {email:<40} {phone:<20} "
        f"{subject:<30} {message:<50} {str(contact.created_at):<25}"
    )

print("=" * 130)

print("-" * 130)
print(f"➡ Total Data Count: {len(all_contact)}")
print("-" * 130)
