"""Module for State class."""
import unittest
from models.state import State
import models
import os.path


class Test_state(unittest.TestCase):
    """Test class for state."""

    def test_name(self):
        """Check if name is empty str."""
        State()
        self.assertEqual(State.name, "")

    def test_name2(self):
        """Check if name is not empty str."""
        State()
        State.name = "California"
        self.assertEqual(State.name, "California")

    def test_save3(self):
        """check if the class is saved in a file."""
        s = State()
        models.storage.new(s)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))


if __name__ == "__main__":
    unittest.main()
