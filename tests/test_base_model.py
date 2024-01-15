#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the BaseModel class
"""


import unittest
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):

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

    def test_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'custom_attribute': 'custom_value'
        }
        custom_model = BaseModel(**kwargs)
        self.assertEqual(custom_model.id, 'test_id')
        self.assertEqual(custom_model.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
