#!/usr/bin/env python3
"""
Test Module for the State Class
"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Test State Class"""

    def test_id(self):
        """ test id """
        self.assertIsInstance(State().id, str)
        self.assertIsInstance(State().created_at, datetime)
        self.assertIsInstance(State().updated_at, datetime)

    def test_name(self):
        """ test name """
        self.assertIsInstance(State().name, str)

    def test_inherit(self):
        """ test inheritance """
        self.assertIsInstance(State(), BaseModel)
        self.assertIsInstance(State(), State)

    def test_to_dict(self):
        """ test to dict """
        self.assertIsInstance(State().to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
