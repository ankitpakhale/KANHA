import os
from alembic import command
from alembic.config import Config
from src.utils import PATH, logger
from sqlalchemy.exc import OperationalError


class MigrationHandler:
    """
    Handles schema migrations programmatically using alembic.
    """

    def __init__(self):
        # initialize alembic configuration
        self.alembic_cfg = Config(os.path.join(PATH.PROJECT_ROOT, "alembic.ini"))
        self.alembic_cfg.set_main_option(
            "script_location", os.path.join(PATH.PROJECT_ROOT, "migrations")
        )

    def initialize_migrations(self):
        """
        Initializes the alembic migrations directory if it doesn't exist.
        """
        # check if the alembic configuration file exists
        if not os.path.exists(self.alembic_cfg.config_file_name):
            logger.error(
                f"Alembic configuration file {
                         self.alembic_cfg.config_file_name} not found."
            )
            return

        try:
            if not os.path.exists(PATH.MIGRATION_PATH):
                logger.debug(
                    "migrations directory not found. initializing migrations..."
                )
                command.init(self.alembic_cfg, PATH.MIGRATION_PATH)
                logger.info("migrations directory initialized successfully.")
            else:
                logger.debug(
                    "migrations directory already exists. skipping initialization."
                )
        except Exception as e:
            logger.error(f"error initializing migrations directory: {e}")
            # raise OperationalError(f"error initializing migrations directory: {e}")  # this line is causing error in further script execution

    def run_migrations(self):
        """
        Runs alembic migrations to apply schema changes.
        """
        try:
            logger.info("applying migrations...")
            command.upgrade(self.alembic_cfg, "head")
            logger.info("migrations applied successfully.")
        except Exception as e:
            logger.error(f"error applying migrations: {e}")
            # raise OperationalError(f"error applying migrations: {e}")  # this line is causing error in further script execution

    # def __apply_all_migrations(self):
    #     """
    #     Apply all migration scripts sequentially from the migrations folder.
    #     """
    #     migration_files = [f for f in os.listdir(PATH.MIGRATION_PATH) if f.endswith(".py")]

    #     if not migration_files:
    #         logger.warning("no migration scripts found.")
    #         return

    #     logger.debug(f"found {len(migration_files)} migration scripts. applying them...")

    #     for migration_file in migration_files:
    #         migration_script_path = os.path.join(
    #             PATH.MIGRATION_PATH, migration_file)
    #         # check the revision
    #         logger.debug(f"applying migration: {migration_file}")
    #         try:
    #             command.upgrade(self.alembic_cfg, migration_script_path)
    #             logger.info(f"migration {migration_file} applied successfully.")
    #         except Exception as e:
    #             print('➡ 76 e:', e)
    #             logger.error(f"error applying migration {migration_file}: {e}")

    def generate_migration(self, message: str):
        """
        Generates a new migration script based on the current model state.
        """
        if not message:
            logger.error("migration description cannot be empty.")
            return

        try:
            # generate the migration script
            logger.info(f"generating migration script for: '{message}'...")
            revision = command.revision(
                self.alembic_cfg, autogenerate=True, message=message
            )

            # check if a migration script was generated
            if revision:
                logger.info(f"migration script generated: {revision}")
            else:
                logger.warning(
                    "migration script generation failed. no changes detected."
                )

            # run the migrations after generating the script
            logger.info("running migrations after generating the script...")
            self.run_migrations()

        except Exception as e:
            logger.error(f"error generating migration script: {e}")
            # raise OperationalError(f"error generating migration script: {e}")  # this line is causing error in further script execution


# main entry point for migration handling
if __name__ == "__main__":
    # initialize migration handler
    migration_handler = MigrationHandler()

    # initialize migrations if not already done
    logger.debug("checking if migrations need to be initialized...")
    migration_handler.initialize_migrations()

    # apply migrations if changes are provided else apply all the existing migrations
    changes = input("describe your changes here: ")

    if changes:
        logger.debug(f"user provided changes: '{changes}'")
        migration_handler.generate_migration(changes)
    else:
        logger.info("no changes provided. applying all migrations...")
        migration_handler.run_migrations()

    logger.debug("migration handler script finished.")
