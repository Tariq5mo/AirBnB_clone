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
        self.assertIsInstance(b.created_at, datetime.datetime)

    def test_time2(self):
        """Test if time is in this form
        %Y-%m-%dT%H:%M:%S.%f
        """
        pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}"
        b = BaseModel()
        self.assertRegex(str(b.created_at), pattern)

    def test_time3(self):
        """Check the time if it is str."""
        b = BaseModel()
        self.assertAlmostEqual(b.created_at, datetime.datetime.now(),
                               delta=datetime.timedelta(seconds=1))

    def test_updated_at(self):
        """
        Check the time of updated_at is
        exactly like created_at at creating time.
        """
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)

    def test_updated_at2(self):
        """Test if time is in this form
        """
        pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}"
        b = BaseModel()
        self.assertRegex(str(b.updated_at), pattern)

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

    def test_save2(self):
        """Check the time of updated_at."""
        b = BaseModel()
        b.save()
        self.assertAlmostEqual(b.updated_at, datetime.datetime.now(),
                               delta=datetime.timedelta(seconds=1))

    def test_save3(self):
        """Test if updated_at is in this form
        %Y-%m-%d %H:%M:%S.%f
        """
        pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}"
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

    def test_to_dict(self):
        """Check the contents"""
        b = BaseModel()
        di = b.to_dict()
        del di["__class__"]
        self.assertCountEqual(b.__dict__.keys(), di.keys())

    def test_to_dict2(self):
        """Check if created_at is str"""
        b = BaseModel()
        self.assertIsInstance(b.to_dict()["created_at"], str)

    def test_to_dict3(self):
        """Check if updated_at is str"""
        b = BaseModel()
        self.assertIsInstance(b.to_dict()["updated_at"], str)

    def test_to_dict4(self):
        """Check if created_at is in form %Y-%m-%dT%H:%M:%S.%f"""
        b = BaseModel()
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"
        self.assertRegex(b.to_dict()["created_at"], pattern)

    def test_to_dict5(self):
        """Check if updated_at is in form %Y-%m-%dT%H:%M:%S.%f"""
        b = BaseModel()
        pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"
        self.assertRegex(b.to_dict()["updated_at"], pattern)

    def test_to_dict6(self):
        """Check if the return of to_dict() is dict"""
        b = BaseModel()
        self.assertIsInstance(b.to_dict(), dict)

    def test_to_dict7(self):
        """Check if the instance is of BaseModel."""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)

    def test_to_dict8(self):
        """Check if __class__ is exists."""
        b = BaseModel()
        self.assertIn("__class__", b.to_dict())

    def test_to_dict9(self):
        """Check the __class__'s value."""
        b = BaseModel()
        self.assertEqual(b.to_dict()["__class__"], b.__class__.__name__)

    def test_to_kwargs(self):
        """Check if kwargs is not empty."""
        i = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        c = '2017-09-28T21:03:54.052298'
        ba = 'BaseModel'
        b = BaseModel(id=i, created_at=c, __class__=ba, my_number=89,
                      updated_at='2017-09-28T21:03:54.052302',
                      name='My_First_Model')
        self.assertCountEqual(
            b.to_dict(), {'id': i, 'created_at': c,
                         '__class__': b.__class__.__name__, 'my_number': 89,
                         'updated_at': '2017-09-28T21:03:54.052302',
                         'name': 'My_First_Model'})

    def test_to_kwargs2(self):
        """Check if kwargs is not empty."""
        i = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        c = '2017-09-28T21:03:54.052298'
        ba = 'BaseModel'
        b = BaseModel(id=i, created_at=c, __class__=ba, my_number=89,
                      updated_at='2017-09-28T21:03:54.052302',
                      name='My_First_Model')
        self.assertCountEqual(
            b.__dict__, {'id': i, 'created_at': c, 'my_number': 89,
                         'updated_at': '2017-09-28T21:03:54.052302',
                         'name': 'My_First_Model'})

    def test_to_kwargs3(self):
        """Check if kwargs is not empty."""
        i = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        c = '2017-09-28T21:03:54.052298'
        ba = 'BaseModel'
        b = BaseModel(id=i, created_at=c, __class__=ba, my_number=89,
                      updated_at='2017-09-28T21:03:54.052302',
                      name='My_First_Model')
        self.assertIsInstance(b, BaseModel)

    def test_to_kwargs4(self):
        """Check if kwargs is not empty."""
        i = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        c = '2017-09-28T21:03:54.052298'
        ba = 'BaseModel'
        b = BaseModel(id=i, created_at=c, __class__=ba, my_number=89,
                      updated_at='2017-09-28T21:03:54.052302',
                      name='My_First_Model')
        self.assertNotIn('__class__', b.__dict__)

    def test_to_kwargs5(self):
        """Check if created_at is datetime."""
        i = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        c = '2017-09-28T21:03:54.052298'
        ba = 'BaseModel'
        b = BaseModel(id=i, created_at=c, __class__=ba, my_number=89,
                      updated_at='2017-09-28T21:03:54.052302',
                      name='My_First_Model')
        self.assertIsInstance(b.created_at, datetime.datetime)

    def test_to_kwargs6(self):
        """Check if updated_at is datetime."""
        i = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        c = '2017-09-28T21:03:54.052298'
        ba = 'BaseModel'
        b = BaseModel(id=i, created_at=c, __class__=ba, my_number=89,
                      updated_at='2017-09-28T21:03:54.052302',
                      name='My_First_Model')
        self.assertIsInstance(b.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
