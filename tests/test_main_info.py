import pytest


@pytest.mark.django_db
def test_get_data(client):
    response = client.get("")
    assert response.status_code == 200
