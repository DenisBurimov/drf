import pytest
from articles.models import Article


@pytest.mark.django_db
def test_get_data(client):
    response = client.get("")
    assert response.status_code == 200
    assert "Django + Tailwind + HTMX" in str(response.content)
    assert "Articles" in str(response.content)

    articles_count = Article.objects.count()
    assert f"for tests: {articles_count}" in str(response.content)


@pytest.mark.django_db
def test_htmx_filters(client):
    response = client.get("")
    assert response.status_code == 200

    article = Article.objects.first()
    response = client.get(
        f"/?search=true&title={article.title}&author={article.author.last_name}&content={article.content[3:7]}"
    )
    assert response.status_code == 200
    assert article.title in str(response.content.decode())

    response = client.get(f"/?search=true&title={article.title}")
    assert response.status_code == 200
    assert article.title in str(response.content.decode())

    response = client.get(f"/?search=true&author={article.author.first_name}")
    assert response.status_code == 200
    assert article.author.first_name in str(response.content.decode())
