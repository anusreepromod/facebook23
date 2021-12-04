from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
# Create your tests here.


class Testsample(TestCase):
    def setup(self):
        self.client = APIClient

    def test_index(self):
        response = self.client.get(reverse('testsample'))
        self.assertEqual(response.status_code, 200)
        print(response.data)
