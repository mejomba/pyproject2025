import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def _tmp_media_settings(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    yield
