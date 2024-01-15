#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up the test environment by clearing the objects dictionary"""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """ Remove the storage file at the end of the tests if it exists """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_empty_objects_initially(self):
        """ Ensure that __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new_object_added_to_objects(self):
        """ Verify that a new object is correctly added to __objects """
        new_object = BaseModel()
        self.assertTrue(new_object in storage.all().values())

    def test_all_returns_dict(self):
        """ Confirm that __objects is properly returned as a dictionary """
        objects_dict = storage.all()
        self.assertIsInstance(objects_dict, dict)

    def test_file_not_created_on_save(self):
        """ Check that a file is not created on BaseModel save """
        self.assertFalse(os.path.exists('file.json'))

    def test_data_saved_to_file(self):
        """ Ensure that data is saved to the file """
        new_object = BaseModel()
        new_object.save()
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_file_storage_save_method(self):
        """ Confirm that the FileStorage save method works """
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_storage_file_loaded_to_objects(self):
        """ Verify that the storage file successfully loaded to __objects"""
        new_object = BaseModel()
        storage.save()
        storage.reload()
        loaded_object = next(iter(storage.all().values()))
        self.assertEqual(new_object.to_dict()['id'],
                         loaded_object.to_dict()['id'])

    def test_reload_from_nonexistent_file(self):
        """ Confirm that nothing happens if the file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save_calls_storage_save(self):
        """ Check that BaseModel save method calls storage save """
        new_object = BaseModel()
        new_object.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_file_path_is_string(self):
        """ Confirm that __file_path is a string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_objects_is_dict(self):
        """ Ensure that __objects is a dictionary """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format_is_correct(self):
        """ Verify that the key is properly formatted """
        new_object = BaseModel()
        _id = new_object.to_dict()['id']
        key = next(iter(storage.all().keys()))
        self.assertEqual(key, f'BaseModel.{_id}')

    def test_storage_object_created(self):
        """ Confirm that the FileStorage object 'storage' is created """
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(storage, FileStorage)


if __name__ == '__main__':
    unittest.main()
