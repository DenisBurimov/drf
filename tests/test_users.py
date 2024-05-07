import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer


@pytest.mark.django_db
def test_get_all_users(client: APIClient):
    response: Response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.data) == User.objects.count()
    assert UserSerializer(response.data[0])


@pytest.mark.django_db
def test_get_user(client: APIClient):
    test_user = User.objects.first()

    assert test_user.phone_number == test_user.phone_number

    response: Response = client.get(f"/users/{test_user.phone_number}")
    assert response.status_code == 200
    assert response.data["phone_number"] == test_user.phone_number


@pytest.mark.django_db
def test_create_user(client: APIClient):
    TEST_PHONE_NUMBER = "1234567890"
    TEST_PASSWORD = "12345"
    TEST_FIRST_NAME = "John"
    TEST_LAST_NAME = "Doe"
    TEST_DESCRIPTION = "Test description"
    user_data = dict(
        phone_number=TEST_PHONE_NUMBER,
        password=TEST_PASSWORD,
        first_name=TEST_FIRST_NAME,
        last_name=TEST_LAST_NAME,
        description=TEST_DESCRIPTION,
    )

    response: Response = client.post("/users/create", user_data, format="json")
    assert response.status_code == 201

    new_user = User.objects.get(phone_number=user_data["phone_number"])
    assert new_user.phone_number == user_data["phone_number"]
    assert new_user.password == user_data["password"]
