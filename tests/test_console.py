#!/usr/bin/python3
""" Tests for console.py """

import os
import sys
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class TestConsole(unittest.TestCase):
    """ Test Console """
    def test_console(self):
        """ Test console """
        self.assertTrue(HBNBCommand())
    
    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

if __name__ == "__main__":
    unittest.main()
