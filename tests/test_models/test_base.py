#!/usr/bin/env python3

"""
Automating tests for the BaseModel
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json

class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class
    """
    def setUp(self):
        """
        Setup Method

        """
        self.base = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base.id, str)
