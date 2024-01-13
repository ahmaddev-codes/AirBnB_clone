#!/usr/bin/python3
"""This module contains a Filestorage class that serializes
instances to a JSON file and deserializes JSON files to
instances
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The file storage engine class:
    A class that serialize and deserialize instances to a JSON file
    """
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }

    def __init__(self):
        """Initialization of a FileStorage Instance"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        if obj.id in self.__objects:
            print("exists")
            return

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = []

        for obj in self.__objects.values():
            new_dict.append(obj.to_dict())

        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""

        # Check if the path to file exists
        if os.path.exists(self.__file_path) is True:
            return

            try:
                with open(self.__file_path, "r") as file:
                    new_obj = json.load(file)

                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        self.__objects[key] = obj
                        # OR - dictionary comprehension
                        # self.__objects =
                        # {key: self.classes[obj['__class__']](**obj) \
                        # for key, obj in loaded_objects.items()}
            except Exception:
                pass
