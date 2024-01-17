#!/usr/bin/env python3
"""
Test Module for the Review Module
"""
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """
    Class for testing the review module
    """
    def setUp(self):
        """
        Set up class
        """
        self.a = Review()
        self.a.place_id = "123"
        self.a.user_id = "123"
        self.a.text = "hello"
        self.b = Review()

    def tearDown(self):
        """
        tear down class
        """
        del self.a
        del self.b

    def test_review_inheritance(self):
        """
        Test Review inheritance
        """
        self.assertIsInstance(self.a, BaseModel)
        self.assertIsInstance(self.a, Review)

    def test_review_attributes(self):
        """
        Test Review attributes
        """
        self.assertEqual(self.a.place_id, "123")
        self.assertEqual(self.a.user_id, "123")
        self.assertEqual(self.a.text, "hello")

    def test_review_id(self):
        """
        Test Review id
        """
        self.assertIsInstance(self.a.id, str)

    def test_attribute_type(self):
        """
        Test attribute type
        """
        self.assertEqual(type(self.a.place_id), str)
        self.assertEqual(type(self.a.user_id), str)
        self.assertEqual(type(self.a.text), str)
        self.assertIsNotNone(self.b.place_id)
        self.assertIsNotNone(self.b.user_id)
        self.assertIsNotNone(self.b.text)

    def test_save(self):
        """
        Test save
        """
        time = self.a.updated_at
        self.a.save()
        self.assertNotEqual(self.a.updated_at, time)


if __name__ == "__main__":
    unittest.main()
