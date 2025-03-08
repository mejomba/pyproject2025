from django.test import TestCase
import uuid
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from aaa.models import CustomUser


class TestCustomUserModel(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {}

    def test_create_user(self):
        CustomUser.objects.create(**self.data)

