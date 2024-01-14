#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class Test_console(unittest.TestCase):
    """Class for testing the console"""

    def setUp(self):
        """Set up the console"""
        self.console = HBNBCommand()
        self.held_output = StringIO()

    def tearDown(self):
        """Clean up after the test"""
        self.held_output.close()

    def capture_output(self):
        """Redirect stdout for capturing output"""
        sys.stdout = self.held_output

    def release_output(self):
        """Restore normal stdout"""
        sys.stdout = sys.__stdout__

    def test_quit(self):
        """Test the quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
