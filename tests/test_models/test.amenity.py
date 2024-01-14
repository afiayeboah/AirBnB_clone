#!/usr/bin/python3

"""
Unit tests for the Amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_inheritance_from_base_model(self):
        """
        Ensure that Amenity inherits from BaseModel.
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_presence_of_name_attribute(self):
        """
        Check if the Amenity class has the 'name' attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_type_of_name_attribute(self):
        """
        Verify that the 'name' attribute of Amenity is of type str.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)


if __name__ == "__main__":
    unittest.main()
