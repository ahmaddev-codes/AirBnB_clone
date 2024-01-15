#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the State class which inherits from the BaseModel
"""


import unittest
from unittest.mock import patch
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_state_inherits_from_base_model(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes_are_set(self):
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)
        self.assertEqual(self.state.name, "")

    def test_state_name_type(self):
        self.assertIsInstance(self.state.name, str)

    @patch('models.storage.save')
    def test_state_save_calls_storage_save_method(self, mock_save):
        self.state.save()
        mock_save.assert_called_once()

    def test_state_str_representation(self):
        expected_str = f"[State] ({self.state.id} {self.state.to_dict()})"
        self.assertEqual(str(self.state), expected_str)

    def test_state_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': 'California',
            'custom_attribute': 'custom_value'
        }
        custom_state = State(**kwargs)
        self.assertEqual(custom_state.id, 'test_id')
        self.assertEqual(custom_state.name, 'California')
        self.assertEqual(custom_state.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
