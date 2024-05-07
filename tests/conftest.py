import os
import pytest
from rest_framework.test import APIClient
from .db import fill_db


@pytest.fixture
def client():
    fill_db()
    yield APIClient()
