#!/usr/bin/env python3
"""
This is the base model

"""
from datetime import datetime
import uuid

class BaseModel():
    """
    THis is the base class

    """
    def __init__(self):
        """
        Initializing the variables
        
        id (int): public instance variables
        created_at: datetime: time when the instance was created
        updated_at: datetime: time when the instance was created

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation
        should print: [<class name>] (<self.id>) <self.__dict__>

        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Method for updating the updated_at public instance attribute

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns the dictionary format of the instance
        """
        air_dict = self.__dict__.copy()
        air_dict['__class__'] = self.__class__.__name__
        air_dict['created_at'] = self.created_at.isoformat()
        air_dict['updated_at'] = self.updated_at.isoformat()
        return air_dict
