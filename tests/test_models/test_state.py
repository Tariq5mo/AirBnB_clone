"""Module for State class."""
import unittest
from models.state import State


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


if __name__ == "__main__":
    unittest.main()
