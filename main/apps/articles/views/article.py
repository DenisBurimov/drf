from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.apps.articles.models.article import Article
from main.apps.articles.serializers import (
    ArticleBaseSerializer,
    ArticleGetSerializer,
    ArticleUpdateSerializer,
)
from main.apps.articles.managers import ArticleManager
from main.logger import log


article_manager = ArticleManager()


@api_view(["GET"])
def get_all_articles(request):
    articles = article_manager.get_all()
    serializer = ArticleGetSerializer(articles, many=True)

    log(log.INFO, "Getting [%d] articles", len(articles))
    return Response(serializer.data)


@api_view(["GET"])
def get_article(request, uuid):
    article = article_manager.get(uuid)
    serializer = ArticleGetSerializer(article)

    log(log.INFO, "Getting article [%s]", uuid)
    return Response(serializer.data)


@api_view(["POST"])
def create_article(request):
    serializer = ArticleBaseSerializer(data=request.data)
    if serializer.is_valid():
        log(log.INFO, "Creating article by author [%s]", serializer.data["author"])
        article, error_message = article_manager.post(serializer.validated_data)
        if not article:
            log(log.ERROR, "Failed to create article: %s", error_message)
            return Response({"error": error_message}, status=400)
        creation_output = ArticleGetSerializer(article)
        return Response(creation_output.data, status=201)

    log(log.ERROR, "Failed to create article")
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def update_article(request, uuid):
    article = Article.objects.get(uuid=uuid)

    if not article:
        log(log.ERROR, "Failed to update article [%s]: article does not exist", uuid)
        return Response({"error": "Article does not exist"}, status=404)

    serializer = ArticleUpdateSerializer(article, data=request.data, partial=True)
    if serializer.is_valid():
        log(log.INFO, "Updating article [%s]", uuid)
        is_updated, error_message = article_manager.put(
            article, serializer.validated_data
        )
        if not is_updated:
            log(log.ERROR, "Failed to update article: %s", error_message)
            return Response({"error": error_message}, status=400)

        updated_output = ArticleGetSerializer(article)
        log(log.INFO, "Updated article [%s]", uuid)
        return Response(updated_output.data)

    log(log.ERROR, "Failed to update article [%s]", uuid)
    return Response(serializer.errors, status=400)
