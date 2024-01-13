#!/usr/bin/python3
"""
This module contains a City class that inherits
from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    name = ""
    state_id = ""
