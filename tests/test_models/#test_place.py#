"""Module for Place test class."""
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """Test class for Place."""

    def test_name(self):
        """Check if name is empty str."""
        Place()
        self.assertEqual(Place.name, "")

    def test_name2(self):
        """Check if name is not empty str."""
        Place()
        Place.name = "California"
        self.assertEqual(Place.name, "California")

    def test_city_id(self):
        """Check if city_id is empty str."""
        Place()
        self.assertEqual(Place.city_id, "")

    def test_city_id2(self):
        """Check if city_id is not empty str."""
        Place()
        Place.city_id = "1234-1234-1234"
        self.assertEqual(Place.city_id, "1234-1234-1234")

    def test_user_id(self):
        """Check if user_id is empty str."""
        Place()
        self.assertEqual(Place.user_id, "")

    def test_user_id2(self):
        """Check if user_id is not empty str."""
        Place()
        Place.user_id = "1234-1234-1234"
        self.assertEqual(Place.user_id, "1234-1234-1234")

    def test_description(self):
        """Check if description is empty str."""
        Place()
        self.assertEqual(Place.description, "")

    def test_description2(self):
        """Check if description is not empty str."""
        Place()
        Place.description = "excellent"
        self.assertEqual(Place.description, "excellent")

    def test_number_rooms(self):
        """Check if number_rooms == 0."""
        Place()
        self.assertEqual(Place.number_rooms, 0)

    def test_number_rooms2(self):
        """Check if number_rooms with assign number."""
        Place()
        Place.number_rooms = 5
        self.assertEqual(Place.number_rooms, 5)

    def test_number_bathrooms(self):
        """Check if number_bathrooms == 0."""
        Place()
        self.assertEqual(Place.number_bathrooms, 0)

    def test_number_bathrooms2(self):
        """Check if number_bathrooms with assign number."""
        Place()
        Place.number_bathrooms = 2
        self.assertEqual(Place.number_bathrooms, 2)

    def test_max_guest(self):
        """Check if max_guest == 0."""
        Place()
        self.assertEqual(Place.max_guest, 0)

    def test_max_guest2(self):
        """Check if max_guest with assign number."""
        Place()
        Place.max_guest = 6
        self.assertEqual(Place.max_guest, 6)

    def test_price_by_night(self):
        """Check if price_by_night == 0."""
        Place()
        self.assertEqual(Place.price_by_night, 0)

    def test_price_by_night2(self):
        """Check if price_by_night with assign number."""
        Place()
        Place.price_by_night = 300
        self.assertEqual(Place.price_by_night, 300)

    def test_latitude(self):
        """Check if latitude == 0."""
        Place()
        self.assertEqual(Place.latitude, 0.0)

    def test_latitude2(self):
        """Check if latitude with assign number."""
        Place()
        Place.latitude = 13.7
        self.assertEqual(Place.latitude, 13.7)

    def test_longitude(self):
        """Check if longitude == 0.0."""
        Place()
        self.assertEqual(Place.longitude, 0.0)

    def test_longitude2(self):
        """Check if longitude with assign number."""
        Place()
        Place.longitude = 20.5
        self.assertEqual(Place.longitude, 20.5)

    def test_amenity_ids(self):
        """Check if amenity_ids is empty list."""
        Place()
        self.assertEqual(Place.amenity_ids, [])

    def test_amenity_ids2(self):
        """Check if amenity_ids with assign number."""
        Place()
        Place.amenity_ids = ["1234", "4321"]
        self.assertEqual(Place.amenity_ids, ["1234", "4321"])


if __name__ == "__main__":
    unittest.main()
