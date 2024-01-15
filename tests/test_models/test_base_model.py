#!/usr/bin/python3

"""
Automating tests for the BaseModel
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


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
        """
        Test id is a string
        """
        self.assertIsInstance(self.base.id, str)

    def test_created_at_is_datetime(self):
        """
        Test created_at is a datetime
        """
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test updated_at is a datetime
        """
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str_representation(self):
        """
        Test string representation
        """
        expected_str = "[BaseModel] ({}) {}".format(self.base.id,
                                                    self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_save_updated_at(self):
        """
        Test save method updates updated_at
        """
        prev_updated_at = self.base.updated_at
        time.sleep(2)
        self.base.save()
        new_updated_at = self.base.updated_at
        self.assertIsNotNone(new_updated_at)
        self.assertNotEqual(prev_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test to_dict method
        """
        expected_dict = {
            'id': self.base.id,
            '__class__': 'BaseModel',
            'created_at': self.base.created_at.isoformat(),
            'updated_at': self.base.updated_at.isoformat()
        }
        self.assertDictEqual(self.base.to_dict(), expected_dict)

    def test_unique_id(self):
        """
        Test id is unique
        """
        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_init_kwargs(self):
        """
        Test init with kwargs
        """
        base_kwargs = BaseModel(id="7757786",
                                created_at="2024-01-01T00:00:00.000000",
                                updated_at="2024-01-01T00:00:00.000000")
        self.assertEqual(base_kwargs.id, "7757786")
        self.assertEqual(base_kwargs.created_at,
                         datetime.fromisoformat("2024-01-01T00:00:00.000000"))
        self.assertEqual(base_kwargs.updated_at,
                         datetime.fromisoformat("2024-01-01T00:00:00.000000"))


if __name__ == "__main__":
    unittest.main()
