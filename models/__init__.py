#!/usr/bin/env python3
"""
Initialization of the models package
ensures that when you import the models package,
an instance of FileStorage is created, and any data stored
in the associated file (if it exists) is loaded into the __objects dictionary
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
