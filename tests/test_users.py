def test_get_user(client):
    response = client.get("/users/get_one")
    assert response.status_code == 200
    assert response.data == {
        "name": "Denys",
        "age": 42,
        "city": "Planet Earth",
    }
