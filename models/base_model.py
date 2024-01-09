#!/usr/bin/python3
"""
This module contains a BaseModel class that defines
all common attributes/methods for other classes
"""


import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base Instance

        Args:
            - *args: list of arguments passes
            - **kwargs: dict of key/value argguments
        """
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"

            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        time_format)
                elif key == 'updated_at':
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        time_format)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        # Copy the class in a new object
        my_dict = self.__dict__.copy()

        # Add '__class__' key with the class name
        my_dict['__class__'] = self.__class__.__name__

        # Convert 'created_at' and 'updated_at' to ISO format strings
        for key, value in my_dict.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = value.isoformat()

        return my_dict

    def __str__(self):
        """Returns a formatted string representation of the instance"""
        class_name = self.__class__.__name__
        attribute_str = str(self.to_dict())
        return f"[{class_name}] ({self.id} {attribute_str})"
