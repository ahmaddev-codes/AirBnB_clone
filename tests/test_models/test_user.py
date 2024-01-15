#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the User class which inherits from the BaseModel
"""


import unittest
from unittest.mock import patch
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_user_inherits_from_base_model(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes_are_set(self):
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_email_password_first_name_last_name_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    @patch('models.storage.save')
    def test_user_save_calls_storage_save_method(self, mock_save):
        self.user.save()
        mock_save.assert_called_once()

    def test_user_str_representation(self):
        expected_str = f"[User] ({self.user.id} {self.user.to_dict()})"
        self.assertEqual(str(self.user), expected_str)

    def test_user_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'email': 'test@example.com',
            'password': 'test_password',
            'first_name': 'John',
            'last_name': 'Doe',
            'custom_attribute': 'custom_value'
        }
        custom_user = User(**kwargs)
        self.assertEqual(custom_user.id, 'test_id')
        self.assertEqual(custom_user.email, 'test@example.com')
        self.assertEqual(custom_user.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
