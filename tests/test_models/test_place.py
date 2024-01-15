#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the Place class which inherits from the BaseModel
"""


import unittest
from unittest.mock import patch
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_place_inherits_from_base_model(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes_are_set(self):
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_types(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    @patch('models.storage.save')
    def test_place_save_calls_storage_save_method(self, mock_save):
        self.place.save()
        mock_save.assert_called_once()

    def test_place_str_representation(self):
        expected_str = f"[Place] ({self.place.id} {self.place.to_dict()})"
        self.assertEqual(str(self.place), expected_str)


if __name__ == '__main__':
    unittest.main()
