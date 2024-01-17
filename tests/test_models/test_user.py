#!/usr/bin/python3
"""unittest module for User class
"""

from datetime import datetime
import unittest
from models import user


class TestUser(unittest.TestCase):
    """
    User class test
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class
        """
        cls.user = user.User()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class
        """
        del cls.user

    def test_id(self):
        """
        Test id
        """
        self.assertEqual(type(self.user.id), str)

    def test_created_at(self):
        """
        Test created_at
        """
        self.assertEqual(type(self.user.created_at), datetime)

    def test_updated_at(self):
        """
        Test updated_at
        """
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_save(self):
        """
        Test save
        """
        time = self.user.updated_at
        self.user.save()
        self.assertNotEqual(time, self.user.updated_at)

    def test_attribute_types(self):
        """
        Test attribute types
        """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_to_dict(self):
        """
        Test to_dict
        """
        user_dict = self.user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertEqual(type(user_dict["__class__"]), str)

    def test_save_with_arg(self):
        """
        Test save with arg
        """
        with self.assertRaises(TypeError):
            self.user.save(None)

    def test_no_arg_instantiates(self):
        """
        no args instantiates
        """
        self.assertEqual(user.User, type(user.User()))
        print("Done")


if __name__ == "__main__":
    unittest.main()
