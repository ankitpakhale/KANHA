import sys
from pathlib import Path

# add the src directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(__path)

from dao import Feedback, db_session  # noqa: E402

# create the session
session = db_session()


def delete_all_feedback():
    """Delete all feedback entries from database"""
    try:
        session.query(Feedback).delete()
        session.commit()
        print("➡ All feedback entries have been deleted.")
    except Exception as e:
        session.rollback()
        print(f"➡ Error occured while deleting all feedback: {e}")


def delete_feedback_by_id(feedback_id):
    """Delete a specific feedback entry by its ID"""
    try:
        feedback_obj = session.query(Feedback).filter_by(id=feedback_id).first()
        if feedback_obj:
            session.delete(feedback_obj)
            session.commit()
            print(f"➡ Feedback with id {feedback_obj} has been deleted.")
        else:
            print(f"➡ No feedback found with id {feedback_obj}.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred while deleting feedback with ID {feedback_id}: {e}")


def main():
    print("Choose an option:")
    print("Press Enter or 0 to delete all feedback entries.")
    print("Press 1 to delete a specific feedback entry by ID.")

    # take user input
    choice = input("Enter your choice: ").strip()

    if choice == "" or choice == "0":
        # user wants to delete all feedback
        delete_all_feedback()
    elif choice == "1":
        # user wants to delete a specific feedback entry by ID
        feedback_id = input("Enter the ID of the feedback you want to delete: ").strip()
        delete_feedback_by_id(feedback_id)
    else:
        print(
            "Invalid choice. Please choose 0 to delete all or 1 to delete specific feedback."
        )


if __name__ == "__main__":
    main()
