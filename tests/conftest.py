import os
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    os.environ["APP_ENV"] = "testing"
    yield APIClient()
    del os.environ["APP_ENV"]
