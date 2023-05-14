from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.


class RegisterUserTest(APITestCase):
    def test_registeruser(self):
        _data = {
            "name": "Kishan",
            "city": "Chennai",
            "dept_id": 1,
            "role_id": 2,
            "salary": 2000000, }

        _response = self.client.post(
            '/api/register/', data=_data, format="json")
        print(_response.status_code)
        _data = _response.json()
        self.assertEqual(_response.status_code, status.HTTP_201_CREATED)
