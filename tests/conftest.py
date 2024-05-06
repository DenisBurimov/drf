import os
import pytest
from rest_framework.test import APIClient
from .db import fill_db


@pytest.fixture
def client():
    os.environ["APP_ENV"] = "testing"
    fill_db()
    yield APIClient()
    del os.environ["APP_ENV"]
