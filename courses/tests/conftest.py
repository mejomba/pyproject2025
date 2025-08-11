import os
import tempfile
import shutil
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def _tmp_media_settings(settings):
    tmpdir = tempfile.mkdtemp(prefix="test_media_")
    settings.MEDIA_ROOT = tmpdir
    yield
    shutil.rmtree(tmpdir, ignore_errors=True)
