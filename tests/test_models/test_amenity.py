#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the Amenity class which inherits from the BaseModel
"""


import unittest
from unittest.mock import patch
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_inherits_from_base_model(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attribute_id(self):
        self.assertIsNotNone(self.amenity.id)

    def test_amenity_attribute_created_at(self):
        self.assertIsNotNone(self.amenity.created_at)

    def test_amenity_attribute_updated_at(self):
        self.assertIsNotNone(self.amenity.updated_at)

    def test_amenity_attribute_name(self):
        self.assertEqual(self.amenity.name, "")

    def test_amenity_name_type(self):
        self.assertIsInstance(self.amenity.name, str)

    @patch('models.storage.save')
    def test_amenity_save_calls_storage_save_method(self, mock_save):
        self.amenity.save()
        mock_save.assert_called_once()

    def test_amenity_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': 'Test Amenity',
            'custom_attribute': 'custom_value'
        }
        custom_amenity = Amenity(**kwargs)
        self.assertEqual(custom_amenity.id, 'test_id')
        self.assertEqual(custom_amenity.name, 'Test Amenity')
        self.assertEqual(custom_amenity.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
