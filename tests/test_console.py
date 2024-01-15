#!/usr/bin/python3
"""This module contains a suite of unittest tests
for the console.py file that controls all operations
of the HBNBcommand project
"""


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hbnb_command = HBNBCommand()

    def test_quit(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_command.onecmd("quit"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.hbnb_command.onecmd("EOF"))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id is missing **")

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id is missing **")

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id is missing **")


if __name__ == '__main__':
    unittest.main()
