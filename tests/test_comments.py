import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from users.models import Profile
from articles.models import Article


@pytest.mark.django_db
def test_comment_create(client: APIClient):
    article = Article.objects.first()
    author = Profile.objects.first()
    comment_data = {
        "text": "Test Comment",
        "author": author.id,
    }
    response: Response = client.post(
        f"/api/articles/comment/{article.uuid}", comment_data
    )
    assert response.status_code == 201
    assert response.data["text"] == comment_data["text"]
    assert response.data["author"] == author.id
    assert response.data["article"] == article.id
