import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer


@pytest.mark.django_db
def test_get_all_articles(client: APIClient):
    response: Response = client.get("/articles/")
    assert response.status_code == 200
    # assert len(response.data) == User.objects.count()
    # assert UserSerializer(response.data[0])
