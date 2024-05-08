import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from users.models import Profile
from articles.models import Article


@pytest.mark.django_db
def test_comment_create(client: APIClient):
    article = Article.objects.first()
    user = Profile.objects.first()
    comment_data = {
        "text": "Test Comment",
        "article": article.uuid,
        "user": user.id,
    }
    response: Response = client.post(f"/articles/comment/{article.uuid}", comment_data)
    assert response.status_code == 201
    assert response.data["text"] == comment_data["text"]
    assert response.data["article"] == str(article.uuid)
    assert response.data["user"] == user.id
