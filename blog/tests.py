from django.test import TestCase
import uuid
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from blog.models import Post


class TestPostModel(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()


