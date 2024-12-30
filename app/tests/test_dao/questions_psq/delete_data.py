import sys
from pathlib import Path

# add the app directory to sys.path
__path = str(Path(__file__).resolve().parent.parent.parent.parent.parent)
sys.path.append(__path)

from app.dao import ProblemSolvingQuestion, db_session  # noqa: E402

# create the session
session = db_session()


def delete_all_psq():
    """Delete all psq entries from database"""
    try:
        print(
            "➡ ===================> Sorry you don't have permission to delete all questions. Try deleting single question"
        )
        # session.query(ProblemSolvingQuestion).delete()
        # session.commit()
        # print("➡ All psq entries have been deleted.")
    except Exception as e:
        session.rollback()
        print(f"➡ Error occured while deleting all psq: {e}")


def delete_psq_by_id(psq_id):
    """Delete a specific psq entry by its ID"""
    try:
        psq_obj = session.query(ProblemSolvingQuestion).filter_by(id=psq_id).first()
        if psq_obj:
            session.delete(psq_obj)
            session.commit()
            print(f"➡ psq with id {psq_obj} has been deleted.")
        else:
            print(f"➡ No psq found with id {psq_obj}.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred while deleting psq with ID {psq_id}: {e}")


def main():
    print("Choose an option:")
    print("Press Enter or 0 to delete all psq entries.")
    print("Press 1 to delete a specific psq entry by ID.")

    # take user input
    choice = input("Enter your choice: ").strip()

    if choice == "" or choice == "0":
        # user wants to delete all psq
        delete_all_psq()
    elif choice == "1":
        # user wants to delete a specific psq entry by ID
        psq_id = input("Enter the ID of the psq you want to delete: ").strip()
        delete_psq_by_id(psq_id)
    else:
        print(
            "Invalid choice. Please choose 0 to delete all or 1 to delete specific psq."
        )


if __name__ == "__main__":
    main()
