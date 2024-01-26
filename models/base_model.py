#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
    self.updated_at = datetime.now()

    def to_dict(self):
        return {
                "__class__": self.__class__.__name__,
                **{key: value.isoformat() if isinstance(value, datetime) else value for key, value in self.__dict__.items()}
                }
