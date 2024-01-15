#!/usr/bin/python3
from models.base_model import BaseModel
""" User Model """


class User(BaseModel):
    """ User Class that inherits from BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
