#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the Review class which inherits from the BaseModel
"""


import unittest
from unittest.mock import patch
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_review_inherits_from_base_model(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes_are_set(self):
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_place_id_user_id_text_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    @patch('models.storage.save')
    def test_review_save_calls_storage_save_method(self, mock_save):
        self.review.save()
        mock_save.assert_called_once()

    def test_review_str_representation(self):
        expected_str = f"[Review] ({self.review.id} {self.review.to_dict()})"
        self.assertEqual(str(self.review), expected_str)

    def test_review_init_with_kwargs(self):
        kwargs = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'place_id': 'test_place_id',
            'user_id': 'test_user_id',
            'text': 'Test review',
            'custom_attribute': 'custom_value'
        }
        custom_review = Review(**kwargs)
        self.assertEqual(custom_review.id, 'test_id')
        self.assertEqual(custom_review.place_id, 'test_place_id')
        self.assertEqual(custom_review.user_id, 'test_user_id')
        self.assertEqual(custom_review.text, 'Test review')
        self.assertEqual(custom_review.custom_attribute, 'custom_value')


if __name__ == '__main__':
    unittest.main()
