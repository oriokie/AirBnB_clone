#!/usr/bin/env python3
""" Place Model """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from models.place import Place


class TestPlaceModule(unittest.TestCase):
    """
    Test Cases for the Place Module
    """
    def test_place_inheritance(self):
        """
        Test Place inheritance
        """
        self.assertIsInstance(Place(), BaseModel)
        self.assertIsInstance(Place(), Place)

    def test_place_attributes(self):
        """
        Test Place attributes
        """
        place = Place()
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_id(self):
        """
        Test Place id
        """
        place = Place()
        self.assertIsInstance(place.id, str)

    def test_place_id_unique(self):
        """
        Test Place id is unique
        """
        place = Place()
        place2 = Place()
        self.assertNotEqual(place.id, place2.id)

    def test_save(self):
        """
        Test save
        """
        place = Place()
        time = place.updated_at
        place.save()
        self.assertNotEqual(time, place.updated_at)


if __name__ == "__main__":
    unittest.main()
