"""Module for Amenity class."""
import unittest
from models.amenity import Amenity


class Test_state(unittest.TestCase):
    """Test class for Amenity."""

    def test_name(self):
        """Check if name is empty str."""
        Amenity()
        self.assertEqual(Amenity.name, "")

    def test_name2(self):
        """Check if name is not empty str."""
        Amenity()
        Amenity.name = "Very good"
        self.assertEqual(Amenity.name, "Very good")


if __name__ == "__main__":
    unittest.main()
