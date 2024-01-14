#!/usr/bin/python3
"""
Simple unittest for BaseModel
"""
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def setUp(self):
        """
        Set up a BaseModel instance
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

        self.my_model = BaseModel()

    def tearDown(self):
        """
        Tear down and clean up
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_id_type(self):
        """
        Check the type of the id attribute
        """
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        """
        Check that ids between two instances are different
        """
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_save(self):
        """
        Check the save method updates updated_at attribute
        """
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_to_dict(self):
        """
        Check the to_dict method returns a dictionary
        """
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)

    def test_kwargs_instantiation(self):
        """
        Test instantiation from dictionary using **kwargs
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)


if __name__ == "__main__":
    unittest.main()
