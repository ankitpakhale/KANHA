import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import MultipleChoiceQuestion, db_session  # noqa: E402

# create the session
session = db_session()


def delete_all_mcq():
    """Delete all mcq entries from database"""
    try:
        print(
            "➡ ===================> Sorry you don't have permission to delete all questions. Try deleting single question"
        )
        # session.query(MultipleChoiceQuestion).delete()
        # session.commit()
        # print("➡ All mcq entries have been deleted.")
    except Exception as e:
        session.rollback()
        print(f"➡ Error occured while deleting all mcq: {e}")


def delete_mcq_by_id(mcq_id):
    """Delete a specific mcq entry by its ID"""
    try:
        mcq_obj = session.query(MultipleChoiceQuestion).filter_by(id=mcq_id).first()
        if mcq_obj:
            session.delete(mcq_obj)
            session.commit()
            print(f"➡ mcq with id {mcq_obj} has been deleted.")
        else:
            print(f"➡ No mcq found with id {mcq_obj}.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred while deleting mcq with ID {mcq_id}: {e}")


def main():
    print("Choose an option:")
    print("Press Enter or 0 to delete all mcq entries.")
    print("Press 1 to delete a specific mcq entry by ID.")

    # take user input
    choice = input("Enter your choice: ").strip()

    if choice == "" or choice == "0":
        # user wants to delete all mcq
        delete_all_mcq()
    elif choice == "1":
        # user wants to delete a specific mcq entry by ID
        mcq_id = input("Enter the ID of the mcq you want to delete: ").strip()
        delete_mcq_by_id(mcq_id)
    else:
        print(
            "Invalid choice. Please choose 0 to delete all or 1 to delete specific mcq."
        )


if __name__ == "__main__":
    main()
