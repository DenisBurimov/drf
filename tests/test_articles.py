import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer


@pytest.mark.django_db
def test_get_all_articles(client: APIClient):
    response: Response = client.get("/articles/")
    assert response.status_code == 200
    assert len(response.data) == Article.objects.count()
    assert ArticleSerializer(response.data[0])
