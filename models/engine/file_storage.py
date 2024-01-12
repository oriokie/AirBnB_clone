#!/usr/bin/env python3
import json
'''from models.base_model import BaseModel'''
"""
This is the file storage Module
"""


class FileStorage:
    """
    This is the file storage class that serializes instances
    to a JSON file and deserializes JSON file to instances

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        - Sets in __objects the obj with key <obj class name>.id
        - It helps in adding a new object to the storage dict _objects
        called whenever a new instance of a class is created
        - it associates the object with a unique key generated
        using the class name and the object's ID

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist
        , no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in FileStorage.__cls__name:
                        self.__objects[key] = self.__cls__name[
                            class_name](**value)

        except Exception:
            pass
