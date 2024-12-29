from app.dao.database.database_manager import db_manager


# initialize the database manager
db_manager = db_manager()
# create tables
db_manager.create_tables()

# create a session
# db_session = db_manager.get_session()
db_session = db_manager.get_session
