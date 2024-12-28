import os
import importlib
from sqlalchemy import inspect, MetaData
from src.dao import models
from utils import PATH


class RegisterModels:
    def __init__(self):
        self.base_model = models.BaseModel

    def __register_or_update_model(self, model_cls):
        """
        Registers the model class to the SQLAlchemy metadata.
        If a model already exists with the same name, its columns will be updated.
        """
        # get the model's table name
        table_name = model_cls.__tablename__

        # inspect the metadata of the table to see if it already exists
        if table_name in self.base_model.metadata.tables:
            # the table already exists, let's update its columns
            print(f"Updating model for table {table_name}")
            existing_table = self.base_model.metadata.tables[table_name]
            for column in model_cls.__table__.columns:
                if column.name not in existing_table.columns:
                    # add new columns to the existing table
                    existing_table.append_column(column)
        else:
            # create the table
            print(f"Registering new model for table {table_name}")
            self.base_model.metadata.create_all(bind=model_cls.__bind_key__)

    def __get_model_files(self):
        return [
            f
            for f in os.listdir(PATH.MODEL_PATH)
            if f.startswith("model_") and f.endswith(".py")
        ]

    def register_models(self):
        """
        Scans the models directory, imports model classes starting with 'model_',
        and registers them in the SQLAlchemy metadata.

        If the model class already exists, it updates the fields.
        """
        # get all files in the models directory and import each model dynamically
        for model_file in self.__get_model_files():
            module_name = f"src.dao.models.{model_file[:-3]}"  # remove .py extension
            module = importlib.import_module(module_name)

            # iterate through all classes in the module
            for class_name in dir(module):
                cls = getattr(module, class_name)

                # check if the class is a subclass of BaseModel
                if (
                    isinstance(cls, type)
                    and issubclass(cls, self.base_model)
                    and cls is not self.base_model
                ):
                    self.__register_or_update_model(cls)
                else:
                    print(f"➡ {cls} is not a model file")
