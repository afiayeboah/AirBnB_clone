#!/usr/bin/python3

"""
Test for the Place model.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Testing Place class.
    """

    def setUp(self):
        """
        Set up an instance of Place for testing.
        """
        self.new_place = Place()

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.new_place

    def test_Place_inheritance(self):
        """
        Test that Place class inherits from BaseModel.
        """
        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes_existence(self):
        """
        Test that Place class contains the expected attributes.
        """
        attributes = ['city_id', 'user_id', 'name', 'description',
                                                    'number_rooms',
                      'number_bathrooms', 'max_guest',
                      'price_by_night', 'latitude',
                      'longitude', 'amenity_ids']
        for attr in attributes:
            self.assertIn(attr, self.new_place.__dir__(),
                          f"Attribute {attr} is missing")

    def test_Place_attributes_type(self):
        """
        Test that Place class attributes have the expected data types.
        """
        self.assertIsInstance(getattr(self.new_place, 'city_id'), str)
        self.assertIsInstance(getattr(self.new_place, 'user_id'), str)
        self.assertIsInstance(getattr(self.new_place, 'name'), str)
        self.assertIsInstance(getattr(self.new_place, 'description'), str)
        self.assertIsInstance(getattr(self.new_place, 'number_rooms'), int)
        self.assertIsInstance(getattr(self.new_place, 'number_bathrooms'), int)
        self.assertIsInstance(getattr(self.new_place, 'max_guest'), int)
        self.assertIsInstance(getattr(self.new_place, 'price_by_night'), int)
        self.assertIsInstance(getattr(self.new_place, 'latitude'), float)
        self.assertIsInstance(getattr(self.new_place, 'longitude'), float)
        self.assertIsInstance(getattr(self.new_place, 'amenity_ids'), list)

    def test_Place_attributes_default_values(self):
        """
        Test that Place class attributes have the expected default values.
        """
        self.assertEqual(getattr(self.new_place, 'city_id'), "")
        self.assertEqual(getattr(self.new_place, 'user_id'), "")
        self.assertEqual(getattr(self.new_place, 'name'), "")
        self.assertEqual(getattr(self.new_place, 'description'), "")
        self.assertEqual(getattr(self.new_place, 'number_rooms'), 0)
        self.assertEqual(getattr(self.new_place, 'number_bathrooms'), 0)
        self.assertEqual(getattr(self.new_place, 'max_guest'), 0)
        self.assertEqual(getattr(self.new_place, 'price_by_night'), 0)
        self.assertEqual(getattr(self.new_place, 'latitude'), 0.0)
        self.assertEqual(getattr(self.new_place, 'longitude'), 0.0)
        self.assertEqual(getattr(self.new_place, 'amenity_ids'), [])
