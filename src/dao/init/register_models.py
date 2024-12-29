from sqlalchemy.exc import SQLAlchemyError
from src.dao import models
from src.utils import PATH, logger
import os
import importlib


# TODO: add this file in utility directory
class RegisterModels:
    def __init__(self):
        self.base_model = models.BaseModel

    def __register_or_update_model(self, model_cls):
        # register new model if table does not exist
        table_name = model_cls.__tablename__
        if table_name in self.base_model.metadata.tables:
            logger.info(f"model for table {table_name} already exists in metadata")
        else:
            try:
                logger.info(f"registering new model for table {table_name}")
                self.base_model.metadata.create_all(bind=model_cls.metadata.bind)
            except SQLAlchemyError as e:
                logger.error(f"error registering model for table {table_name}: {e}")

    def __get_model_files(self):
        # get all model files in the models directory
        model_files = [
            f
            for f in os.listdir(PATH.MODEL_PATH)
            if f.startswith("model_") and f.endswith(".py")
        ]
        if not model_files:
            msg = "No model files found"
            logger.error(msg)
            raise FileNotFoundError(msg)

        # if model_files then simply return it
        return model_files

    def __register_models(self):
        # dynamically import and register models
        for model_file in self.__get_model_files():
            module_name = f"{PATH.MODEL_PATH.replace('/', '.')}.{model_file[:-3]}"
            try:
                module = importlib.import_module(module_name)
            except ImportError as e:
                logger.error(f"failed to import module {module_name}: {e}")
                continue

            for class_name in dir(module):
                cls = getattr(module, class_name)
                if (
                    isinstance(cls, type)
                    and issubclass(cls, self.base_model)
                    and cls is not self.base_model
                ):
                    logger.info(f"registering model class: {cls.__name__}")
                    self.__register_or_update_model(cls)

    def register_models(self):
        # main entry point for registering models
        logger.info("starting model registration process")
        self.__register_models()
        logger.info("model registration process completed")


# main entry point
if __name__ == "__main__":
    register_models = RegisterModels()
    register_models.register_models()
