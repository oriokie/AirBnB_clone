import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines the unit tests for file_storage"""

    @classmethod
    def setUpClass(cls):

        file_path = "file.json"
        if os.path.exists(file_path):
            os.remove(file_path)

        # Clear the __objects dictionary
        FileStorage.__objects = {}
        cls.storage = FileStorage()
        cls.storage.reload()
        cls.name_mapping = {'BaseModel': BaseModel}

    @classmethod
    def tearDownClass(cls):
        all_objs = cls.storage.all()
        all_objs.clear()
        cls.storage.save()

    def test_all_method_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_if_obj_in_dictionary(self):
        new_instance = BaseModel()
        class_name = new_instance.__class__.__name__
        key = f"{class_name}.{new_instance.id}"
        self.assertIsInstance(self.storage.all()[key],
                              self.name_mapping[class_name])

    def test_instance_creation_adds_to_storage(self):
        new_instance = BaseModel()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        self.assertIn(key, self.storage.all())

    def test_storage_file_path_is_str(self):
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_reload_json_has_something(self):
        new_instance = BaseModel()
        new_instance.save()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"

        self.storage.reload()
        all_objs = self.storage.all()

        self.assertIsInstance(all_objs[key], BaseModel)

    def test_new_method_adds_instance_to_storage(self):
        new_instance = BaseModel()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
