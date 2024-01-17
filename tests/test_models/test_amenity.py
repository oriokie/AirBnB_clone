#!/usr/bin/python3
"""
Test Module for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenity(unittest.TestCase):
    """
    Class for testing the amenity module
    """
    @classmethod
    def setUpClass(cls):
        """ Set up class """
        cls.amenity_instance = Amenity()
        cls.amenity_instance.name = "test"
        cls.another_amenity_instance = Amenity()
    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        del cls.amenity_instance
        del cls.another_amenity_instance
        try:
            os.remove("file.json")
        except:
            pass
    def test_name(self):
        """ Test name """
        self.assertEqual(self.amenity_instance.name, "test")
        self.assertEqual(self.another_amenity_instance.name, "")
    def test_id(self):
        """ Test id """
        self.assertIsInstance(self.amenity_instance.id, str)
        self.assertIsInstance(self.another_amenity_instance.id, str)
    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.amenity_instance, Amenity)
        self.assertIsInstance(self.another_amenity_instance, Amenity)
    def test_save(self):
        """ Test save """
        time = self.amenity_instance.updated_at
        self.amenity_instance.save()
        self.assertNotEqual(time, self.amenity_instance.updated_at)
        self.assertNotEqual(time, self.another_amenity_instance.updated_at)
        self.assertNotEqual(self.amenity_instance.id, self.another_amenity_instance.id)
        self.assertNotEqual(self.amenity_instance.created_at, self.another_amenity_instance.created_at)
        self.assertNotEqual(self.amenity_instance.updated_at, self.another_amenity_instance.updated_at)
        self.assertNotEqual(self.amenity_instance.__dict__, self.another_amenity_instance.__dict__)
    
    def test_to_dict(self):
        """ Test to_dict """
        self.assertIsInstance(self.amenity_instance.to_dict(), dict)
        self.assertIsInstance(self.another_amenity_instance.to_dict(), dict)

    def test_inherit(self):
        """ Test inheritance """
        self.assertIsInstance(self.amenity_instance, BaseModel)
        self.assertIsInstance(self.another_amenity_instance, BaseModel)


if __name__ == '__main__':
    unittest.main()
