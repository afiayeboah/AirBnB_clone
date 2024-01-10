#!/usr/bin/python3

"""
Unit tests for the Review model.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_inheritance_from_base_model(self):
        """
        Verify that the Review class inherits from BaseModel.
        """
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_presence_of_attributes(self):
        """
        Ensure that the Review class has
        'place_id', 'user_id', and 'text' attributes.
        """
        new_review = Review()
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

    def test_data_type_of_attributes(self):
        """
        Confirm that the 'place_id', 'user_id', and 'text'
        attributes in the Review class
        are of type str.
        """
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text_value = getattr(new_review, "text")
        self.assertIsInstance(place_id_value, str)
        self.assertIsInstance(user_id_value, str)
        self.assertIsInstance(text_value, str)


if __name__ == "__main__":
    unittest.main()
