"""Module for Review test class."""
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """Test class for Review."""

    def test_user_id(self):
        """Check if user_id is empty str."""
        Review()
        self.assertEqual(Review.user_id, "")

    def test_user_id2(self):
        """Check if user_id is not empty str."""
        Review()
        Review.user_id = "1234-1234-1234"
        self.assertEqual(Review.user_id, "1234-1234-1234")

    def test_place_id(self):
        """Check if place_id is empty str."""
        Review()
        self.assertEqual(Review.place_id, "")

    def test_place_id2(self):
        """Check if place_id is not empty str."""
        Review()
        Review.place_id = "1234-1234-1234"
        self.assertEqual(Review.place_id, "1234-1234-1234")

    def test_text(self):
        """Check if text is empty str."""
        Review()
        self.assertEqual(Review.text, "")

    def test_text2(self):
        """Check if text is not empty str."""
        Review()
        Review.text = "1234-1234-1234"
        self.assertEqual(Review.text, "1234-1234-1234")


if __name__ == "__main__":
    unittest.main()
