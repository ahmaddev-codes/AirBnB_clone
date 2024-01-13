#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the BaseModel class
"""


import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest tests for the BaseModel class"""

    def setUp(self):
        self.Model = BaseModel()
        self.new_Model = BaseModel()

    def test_model_id(self):
        self.Model.id = uuid.uuid4()
        self.new = self.Model.id
        self.assertEqual(self.Model.id, self.new)

    def test_model_name(self):
        self.Model.name = "My First Model"
        self.assertEqual(self.Model.name, "My First Model")

    def test_model_num(self):
        self.Model.num = 89
        self.assertEqual(self.Model.num, 89)

    def test_model_to_dict(self):
        self.Model_json = self.Model.to_dict()
        self.assertEqual(self.Model_json, self.Model.to_dict())

    def test_model_attr(self):
        self.Model_class_name = self.Model.__class__.__name__
        self.assertEqual(self.Model_class_name, "BaseModel")

    def test_model_instance(self):
        self.assertFalse(self.new_Model is self.Model)

    def test_kwargs(self):
        self.assertTrue()


if __name__ == "__main__":
    unittest.main()
