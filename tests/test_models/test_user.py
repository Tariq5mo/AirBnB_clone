import unittest
from models.user import User


class Test_base_model(unittest.TestCase):
    """Test class"""

    def test_email(self):
        """check if email is empty."""
        User()
        self.assertEqual(User.email, "")

    def test_email2(self):
        """check if email is not empty."""
        User()
        User.email = "exanple@email.com"
        self.assertEqual(User.email, "exanple@email.com")

    def test_password(self):
        """check if password is empty."""
        User()
        self.assertEqual(User.password, "")

    def test_password2(self):
        """check if password is not empty."""
        User()
        User.password = "0123456789"
        self.assertEqual(User.password, "0123456789")

    def test_first_name(self):
        """check if first_name is empty."""
        User()
        self.assertEqual(User.first_name, "")

    def test_first_name2(self):
        """check if first_name is not empty."""
        User()
        User.first_name = "jack"
        self.assertEqual(User.first_name, "jack")

    def test_last_name(self):
        """check if last_name is empty."""
        User()
        self.assertEqual(User.last_name, "")

    def test_last_name2(self):
        """check if last_name is not empty."""
        User()
        User.last_name = "milan"
        self.assertEqual(User.last_name, "milan")


if __name__ == "__main__":
    unittest.main()
