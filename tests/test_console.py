#!/usr/bin/python3
""" Tests for console.py """

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Test Console """
    def test_console(self):
        """ Test console """
        self.assertTrue(HBNBCommand())


if __name__ == "__main__":
    unittest.main()
