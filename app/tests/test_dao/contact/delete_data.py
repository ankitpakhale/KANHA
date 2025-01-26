import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import Contact, db_session  # noqa: E402

# create the session
session = db_session()


def delete_all_contact():
    """Delete all contact entries from database"""
    try:
        session.query(Contact).delete()
        session.commit()
        print("➡ All contact entries have been deleted.")
    except Exception as e:
        session.rollback()
        print(f"➡ Error occured while deleting all contact: {e}")


def delete_contact_by_id(contact_id):
    """Delete a specific contact entry by its ID"""
    try:
        contact_obj = session.query(Contact).filter_by(id=contact_id).first()
        if contact_obj:
            session.delete(contact_obj)
            session.commit()
            print(f"➡ Contact with id {contact_obj} has been deleted.")
        else:
            print(f"➡ No contact found with id {contact_obj}.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred while deleting contact with ID {contact_id}: {e}")


def main():
    print("Choose an option:")
    print("Press Enter or 0 to delete all contact entries.")
    print("Press 1 to delete a specific contact entry by ID.")

    # take user input
    choice = input("Enter your choice: ").strip()

    if choice == "" or choice == "0":
        # user wants to delete all contact
        delete_all_contact()
    elif choice == "1":
        # user wants to delete a specific contact entry by ID
        contact_id = input("Enter the ID of the contact you want to delete: ").strip()
        delete_contact_by_id(contact_id)
    else:
        print(
            "Invalid choice. Please choose 0 to delete all or 1 to delete specific contact."
        )


if __name__ == "__main__":
    main()
