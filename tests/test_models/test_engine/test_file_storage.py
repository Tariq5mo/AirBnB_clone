"""Test module for FileStorage file"""
import unittest
from models.base_model import BaseModel
import models
import os.path


class Test_FileStorage(unittest.TestCase):
    """Test class for FileStorage."""

    def test_file_path(self):
        """Test the file path if it's str."""
        sto = models.storage
        self.assertIsInstance(sto._FileStorage__file_path, str)

    def test_file_path2(self):
        """Test the file path if it's file.json."""
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")

    def test_file_path3(self):
        """Test the file path if it ends with (.json)."""
        r = ".json$"
        self.assertRegex(models.storage._FileStorage__file_path, r)

    def test_objects(self):
        """Check if __objects is dict."""
        self.assertIsInstance(models.storage._FileStorage__objects, dict)

    def test_objects2(self):
        """Check if __objects is empty dict."""
        models.storage._FileStorage__objects = {}
        self.assertEqual(models.storage._FileStorage__objects, {})

    def test_all(self):
        """Check the return value of all() method."""
        self.assertIsInstance(models.storage.all(), dict)

    def test_new(self):
        """Check the content of __objects."""
        b = BaseModel()
        models.storage.new(b)
        keylist = models.storage._FileStorage__objects
        key = keylist[f"{b.__class__.__name__}.{b.id}"]
        self.assertEqual(key, b)

    def test_save(self):
        """Check the save method."""
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload(self):
        """Check the reload method."""
        models.storage.reload()
        self.assertIsInstance(models.storage._FileStorage__objects, dict)


if __name__ == "__main__":
    unittest.main()
