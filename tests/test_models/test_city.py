#!/usr/bin/python3
"""
Test City Module
"""
from models.city import City
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    class for testing the city module
    """

    @classmethod
    def setUpClass(cls):
        """ set up class """
        cls.city_instance = City()
        cls.city_instance.name = "test"
        cls.city_instance.state_id = "test"

    @classmethod
    def tearDownClass(cls):
        """ tear down class """
        del cls.city_instance

    def test_name(self):
        """ test name """
        self.assertEqual(self.city_instance.name, "test")
        self.assertEqual(self.city_instance.state_id, "test")

    def test_id(self):
        """ test id """
        self.assertIsInstance(self.city_instance.id, str)
        self.assertIsInstance(self.city_instance.created_at, datetime)
        self.assertIsInstance(self.city_instance.updated_at, datetime)

    def test_instance(self):
        """ test instance """
        self.assertIsInstance(self.city_instance, City)
        self.assertIsInstance(self.city_instance, BaseModel)

    def test_save(self):
        """ test save """
        time = self.city_instance.updated_at
        self.city_instance.save()
        self.assertNotEqual(time, self.city_instance.updated_at)
        '''self.assertNotEqual(time, self.city_instance.created_at)'''
        self.assertNotEqual(self.city_instance.created_at,
                            self.city_instance.updated_at)

    def test_to_dict(self):
        """ test to dict """
        self.assertIsInstance(self.city_instance.to_dict(), dict)
        self.assertIsInstance(self.city_instance.to_dict(), dict)

    def test_inherit(self):
        """ test inheritance """
        self.assertIsInstance(self.city_instance, BaseModel)
        self.assertIsInstance(self.city_instance, BaseModel)


if __name__ == "__main__":
    unittest.main()
