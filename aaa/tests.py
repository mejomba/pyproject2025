from django.test import TestCase
from rest_framework.test import APIClient
from aaa.models.user_models import CustomUser


class TestCustomUserModel(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {}

    def test_create_user(self):
        CustomUser.objects.create(**self.data)

