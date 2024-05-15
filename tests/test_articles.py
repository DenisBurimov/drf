import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from main.apps.users.models import Profile
from main.apps.articles.models import Article
from main.apps.articles.serializers import ArticleBaseSerializer


@pytest.mark.django_db
def test_get_all_articles(client: APIClient):
    response: Response = client.get("/api/articles/")
    assert response.status_code == 200
    assert len(response.data) == Article.objects.count()
    assert ArticleBaseSerializer(response.data[0])


@pytest.mark.django_db
def test_get_article(client: APIClient):
    article = Article.objects.first()
    response: Response = client.get(f"/api/articles/{article.uuid}")
    assert response.status_code == 200
    assert ArticleBaseSerializer(response.data)
    assert response.data["uuid"] == str(article.uuid)
    assert response.data["title"] == article.title
    assert response.data["content"] == article.content
    assert response.data["author"] == article.author_id


@pytest.mark.django_db
def test_create_article(client: APIClient):
    article_data = {
        "title": "Test Article",
        "content": "This is a test article",
        "author": 1,
    }
    response: Response = client.post("/api/articles/create", article_data)
    assert response.status_code == 201
    assert Article.objects.filter(uuid=response.data["uuid"]).exists()
    assert response.data["title"] == article_data["title"]
    assert response.data["content"] == article_data["content"]
    assert response.data["author"] == article_data["author"]


@pytest.mark.django_db
def test_update_article(client: APIClient):
    article = Article.objects.first()
    article_data = {
        "title": "Updated Article",
        "content": "This is an updated article",
    }
    response: Response = client.put(
        f"/api/articles/update/{article.uuid}", article_data
    )
    assert response.status_code == 200
    assert response.data["title"] == article_data["title"]
    assert response.data["content"] == article_data["content"]
    assert response.data["author"] == article.author_id
    assert Article.objects.get(uuid=article.uuid).title == article_data["title"]
    assert Article.objects.get(uuid=article.uuid).content == article_data["content"]

    TEST_LIKERS_NUMBER = 2
    likers = Profile.objects.exclude(id=1).order_by("?")[:TEST_LIKERS_NUMBER]

    for liker in likers:
        assert liker.id != article.author_id
    assert len(likers) == TEST_LIKERS_NUMBER

    likes_data = {
        "users_liked": [likers[0].id],
    }

    response: Response = client.put(f"/api/articles/update/{article.uuid}", likes_data)
    assert response.status_code == 200
    assert response.data["users_liked"] == [likers[0].id]
    assert article.users_liked.count() == 1

    likers_data = {
        "users_liked": [likers[1].id],
    }
    response: Response = client.put(f"/api/articles/update/{article.uuid}", likers_data)
    assert response.status_code == 200
    assert article.users_liked.count() == 2
