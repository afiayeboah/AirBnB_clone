#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
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
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("sys.stdin", StringIO("quit\n")):
                self.console.cmdloop()
                self.assertEqual(mock_stdout.getvalue().strip(), "")
    
    def test_EOF(self):
        """Test the EOF command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("sys.stdin", StringIO("EOF\n")):
                self.console.cmdloop()
                self.assertEqual(mock_stdout.getvalue().strip(), "")

if __name__ == "__main__":
    unittest.main()

