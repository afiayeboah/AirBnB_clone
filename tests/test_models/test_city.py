#!/usr/bin/python3
"""
Module for City unittest
"""
import os
import unittest
from datetime import datetime, timedelta
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unittests for City class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        city = City()
        self.assertEqual(City, type(city))
        self.assertEqual(str, type(city.id))
        self.assertEqual(datetime, type(city.created_at))
        self.assertEqual(datetime, type(city.updated_at))
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(City))
        self.assertNotIn("state_id", city.__dict__)
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(City))
        self.assertNotIn("name", city.__dict__)

    def test_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_created_updated_at(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        city = City()
        city.id = "777777"
        city.created_at = city.updated_at = my_date
        city_str = str(city)
        self.assertIn("[City] (777777)", city_str)
        self.assertIn("'id': '777777'", city_str)
        self.assertIn("'created_at': {}".format(repr(my_date)), city_str)
        self.assertIn("'updated_at': {}".format(repr(my_date)), city_str)

    def test_save_method(self):
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_save_updates_file(self):
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())

    def test_to_dict_method(self):
        city = City()
        city.middle_name = "Johnson"
        city.my_number = 777
        city_dict = city.to_dict()
        self.assertTrue(dict, type(city_dict))
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual("Johnson", city_dict["middle_name"])
        self.assertIn("my_number", city_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = my_date
        to_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), to_dict)


if __name__ == "__main__":
    unittest.main()
