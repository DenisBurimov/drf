import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from users.models import D3User


@pytest.mark.django_db
def test_get_user(client: APIClient):
    TEST_USER_PHONE_NUMBER = "1234567890"
    TEST_USER_PASSWORD = "password"
    D3User.objects.create(
        phone_number=TEST_USER_PHONE_NUMBER,
        password=TEST_USER_PASSWORD,
    )

    test_user = D3User.objects.first()

    assert test_user.phone_number == TEST_USER_PHONE_NUMBER

    response: Response = client.get(f"/users/{TEST_USER_PHONE_NUMBER}")
    assert response.status_code == 200
    assert response.data["phone_number"] == TEST_USER_PHONE_NUMBER
