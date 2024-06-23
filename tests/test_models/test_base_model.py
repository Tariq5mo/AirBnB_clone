"""Test module for base_model.py file"""
import unittest
from models.base_model import BaseModel
import datetime


class Test_base_model(unittest.TestCase):
    """Test class"""

    def test_id_str(self):
        """Test if id is str."""
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_id_form(self):
        """Test if id is in this form
        xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx
        """
        pattern = r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}"
        b = BaseModel()
        self.assertRegex(b.id, pattern)

    def test_id_change(self):
        """Test change id to str."""
        b = BaseModel()
        b.id = "Try"
        self.assertEqual(b.id, "Try")

    def test_id_change2(self):
        """Test change id to int."""
        b = BaseModel()
        b.id = 123
        self.assertEqual(b.id, 123)

    def test_id_change3(self):
        """Test change id to float."""
        b = BaseModel()
        b.id = 1.2
        self.assertEqual(b.id, 1.2)

    def test_id_change4(self):
        """Test change id to list."""
        b = BaseModel()
        b.id = [1, 2]
        self.assertEqual(b.id, [1, 2])

    def test_id_change5(self):
        """Test change id to tuple."""
        b = BaseModel()
        b.id = (1, 2)
        self.assertEqual(b.id, (1, 2))

    def test_id_change6(self):
        """Test change id to set."""
        b = BaseModel()
        b.id = {1, 2}
        self.assertEqual(b.id, {1, 2})

    def test_id_change7(self):
        """Test change id to dict."""
        b = BaseModel()
        b.id = {1: 15, 2: 15}
        self.assertEqual(b.id, {1: 15, 2: 15})

    def test_id_change8(self):
        """Test change id to bool."""
        b = BaseModel()
        b.id = True
        self.assertEqual(b.id, True)

    def test_time(self):
        """Check the time if it is str."""
        b = BaseModel()
        self.assertIsInstance(b.created_at, str)

    '''def test_time2(self):
        """Test if time is in this form
        %Y-%m-%dT%H:%M:%S.%f
        """
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"
        b = BaseModel()
        self.assertRegex(str(b.created_at), pattern)'''

    def test_time3(self):
        """Check the time if it is str."""
        b = BaseModel()
        self.assertEqual(b.created_at,
                         datetime.datetime.now())

    def test_updated_at(self):
        """
        Check the time of updated_at is
        exactly like created_at at creating time.
        """
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)

    def test_updated_at2(self):
        """Test if time is in this form
        %Y-%m-%dT%H:%M:%S.%f
        """
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"
        b = BaseModel()
        self.assertRegex(b.updated_at, pattern)

    def test_str(self):
        """Check the str of the class."""
        b = BaseModel()
        self.assertEqual(b.__str__(),
                         f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}")

    def test_str2(self):
        """Check the str of the class."""
        b = BaseModel()
        self.assertIsInstance(b.__str__(), str)

    def test_save(self):
        """Check updated_at != created_at after use save()."""
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    '''def test_save2(self):
        """Check the time of updated_at."""
        b = BaseModel()
        b.save()
        self.assertAlmostEqual(b.updated_at,
                                datetime.datetime.now())'''

    def test_save3(self):
        """Test if updated_at is in this form
        %Y-%m-%dT%H:%M:%S.%f
        """
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"
        b = BaseModel()
        b.save
        self.assertRegex(str(b.updated_at), pattern)

    def test_save4(self):
        """Check the time of updated_at last and continue."""
        b = BaseModel()
        first_updated_at = b.updated_at
        b.save()
        second_updated_at = b.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)

if __name__ == "__main__":
    unittest.main()
