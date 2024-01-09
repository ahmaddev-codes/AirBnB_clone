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
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        result_dict = self.__dict__.copy()

        # Add '__class__' key with the class name
        result_dict['__class__'] = self.__class__.__name__

        # Convert 'created_at' and 'updated_at' to ISO format strings
        for key, value in result_dict.items():
            if key in ['created_at', 'updated_at']:
                result_dict[key] = value.isoformat()

        return result_dict

    def __str__(self):
        """Returns a formatted string representation of the instance"""
        class_name = self.__class__.__name__
        instance_id = self.id
        attribute_str = str(self.to_dict())
        return f"[{class_name}] ({instance_id} {attribute_str})"
