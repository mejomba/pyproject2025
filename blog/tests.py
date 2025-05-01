from django.test import TestCase
from rest_framework.test import APIClient


class TestPostModel(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()


