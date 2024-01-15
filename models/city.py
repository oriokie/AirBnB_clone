#!/usr/bin/python3
""" City Model"""
from models.base_model import BaseModel


class City(BaseModel):
    """ city class that inherits from Basemodel """
    state_id = ""
    name = ""
