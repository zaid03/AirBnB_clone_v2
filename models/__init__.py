#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import environ as env


from os import getenv

storage_env = getenv("HBNB_TYPE_STORAGE")
if storage_env == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
