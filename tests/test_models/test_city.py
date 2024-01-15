#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the City class which inherits from the BaseModel
"""


import unittest
from unittest.mock import patch
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_city_inherits_from_base_model(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes_are_set(self):
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_city_name_state_id_types(self):
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    @patch('models.storage.save')
    def test_city_save_calls_storage_save_method(self, mock_save):
        self.city.save()
        mock_save.assert_called_once()

    def test_city_str_representation(self):
        expected_str = f"[City] ({self.city.id} {self.city.to_dict()})"
        self.assertEqual(str(self.city), expected_str)

    def test_city_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': 'Test City',
            'state_id': 'test_state_id',
            'custom_attribute': 'custom_value'
        }
        custom_city = City(**kwargs)
        self.assertEqual(custom_city.id, 'test_id')
        self.assertEqual(custom_city.name, 'Test City')
        self.assertEqual(custom_city.state_id, 'test_state_id')
        self.assertEqual(custom_city.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
