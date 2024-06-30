"""Module for City class."""
import unittest
from models.state import State
from models.city import City


class Test_City(unittest.TestCase):
    """Test class for City."""

    def test_name(self):
        """Check if name is empty str."""
        City()
        self.assertEqual(City.name, "")

    def test_name2(self):
        """Check if name is not empty str."""
        City()
        City.name = "San Francisco"
        self.assertEqual(City.name, "San Francisco")

    def test_state_id(self):
        """Check if state_id is empty str."""
        City()
        self.assertEqual(City.state_id, "")

    def test_state_id2(self):
        """Check if state_id is not empty str."""
        City()
        State()
        State.id = "1234-1234-1234"
        City.state_id = "1234-1234-1234"
        self.assertEqual(City.state_id, "1234-1234-1234")


if __name__ == "__main__":
    unittest.main()
