from http.client import responses

from rest_framework.test import APITestCase
from .models import Amenity, Room
from users.models import User

# Create your tests here.

class TestAmenities(APITestCase):

    NAME = 'Test Amenity'
    DESCRIPTION = 'Test Description'

    URL ="/api/v1/rooms/amenities/"

    def setUp(self):
        Amenity.objects.create(name=self.NAME, description=self.DESCRIPTION)

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        self.assertIsInstance(data, list, f"Expected list, but got {type(data)}")
        self.assertEqual(len(data), 1, f"Expected 1, but got {len(data)}")
        self.assertEqual(data[0]['name'], self.NAME, f"Expected {self.NAME}, but got {data[0]['name']}")
        self.assertEqual(data[0]['description'], self.DESCRIPTION, f"Expected {self.DESCRIPTION}, but got {data[0]['description']}")

    def test_create_amenity(self):
        NAME = 'New Amenity'
        DESCRIPTION = 'New Description'
        post_data = {
            'name': NAME,
            'description': DESCRIPTION
        }
        response = self.client.post(self.URL, data=post_data)
        data = response.json()
        self.assertEqual(response.status_code, 200, f"Expected 201, but got {response.status_code}")
        self.assertEqual(data['name'], NAME, f"Expected {NAME}, but got {data['name']}")
        self.assertEqual(data['description'], DESCRIPTION, f"Expected {DESCRIPTION}, but got {data['description']}")

        response = self.client.post(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, 400, f"Expected 400, but got {response.status_code}")
        self.assertIn('name', data, f"Expected 'name' in {data}")


class TestAmenity(APITestCase):

    NAME = 'Test Amenity'
    DESCRIPTION = 'Test Description'

    URL = "/api/v1/rooms/amenities/1/"

    def setUp(self):
        Amenity.objects.create(name=self.NAME, description=self.DESCRIPTION)

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2/")
        self.assertEqual(response.status_code, 404, f"Expected 404, but got {response.status_code}")

    def test_get_amenity(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        self.assertEqual(data['name'], self.NAME, f"Expected {self.NAME}, but got {data['name']}")
        self.assertEqual(data['description'], self.DESCRIPTION, f"Expected {self.DESCRIPTION}, but got {data['description']}")

    def test_put_amenity(self):
        NAME = 'New Amenity'
        DESCRIPTION = 'New Description'
        post_data = {
            'name': NAME,
            'description': DESCRIPTION
        }
        response = self.client.put(self.URL, data=post_data)
        data = response.json()
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")
        self.assertEqual(data['name'], NAME, f"Expected {NAME}, but got {data['name']}")
        self.assertEqual(data['description'], DESCRIPTION, f"Expected {DESCRIPTION}, but got {data['description']}")

        post_data = {
            'name': "over 150 characters" * 10,
        }
        response = self.client.put(self.URL, data=post_data)
        data = response.json()
        self.assertEqual(response.status_code, 400, f"Expected 400, but got {response.status_code}")
        self.assertIn('name', data, f"Expected 'name' in {data}")

    def test_delete_amenity(self):
        response = self.client.delete(self.URL)
        self.assertEqual(response.status_code, 204, f"Expected 204, but got {response.status_code}")
        # response = self.client.get(self.URL)
        # self.assertEqual(response.status_code, 404, f"Expected 404, but got {response.status_code}")


class TestRooms(APITestCase):

    URL = "/api/v1/rooms/"

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('testpassword')
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 403, f"Expected 403, but got {response.status_code}")

        self.client.force_login(self.user)
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 400, f"Expected 400, but got {response.status_code}")