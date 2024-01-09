import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up a User instance for testing."""
        self.new_user = User()

    def test_user_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(self.new_user, BaseModel)

    def test_user_attributes_exist(self):
        """Test that User has the required attributes."""
        attributes = ['email', 'first_name', 'last_name', 'password']
        for attr in attributes:
            with self.subTest(attribute=attr):
                self.assertTrue(hasattr(self.new_user, attr))

    def test_email_type(self):
        """Test the type of the email attribute."""
        self.assertIsInstance(self.new_user.email, str)

    def test_first_name_type(self):
        """Test the type of the first_name attribute."""
        self.assertIsInstance(self.new_user.first_name, str)

    def test_last_name_type(self):
        """Test the type of the last_name attribute."""
        self.assertIsInstance(self.new_user.last_name, str)

    def test_password_type(self):
        """Test the type of the password attribute."""
        self.assertIsInstance(self.new_user.password, str)


if __name__ == '__main__':
    unittest.main()
