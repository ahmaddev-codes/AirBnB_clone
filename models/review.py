#!/usr/bin/python3
"""
This module contains a Review class that inherits
from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
