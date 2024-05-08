from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models.article import Article
from .serializers import ArticleBaseSerializer, ArticleGetSerializer
from .managers import create_new_article
from d3.logger import log


@api_view(["GET"])
def get_all_articles(request):
    articles = Article.objects.all()
    serializer = ArticleGetSerializer(articles, many=True)

    log(log.INFO, "Getting [%d] articles", len(articles))
    return Response(serializer.data)


@api_view(["GET"])
def get_article(request, uuid):
    article = Article.objects.get(uuid=uuid)
    serializer = ArticleGetSerializer(article)

    log(log.INFO, "Getting article [%s]", uuid)
    return Response(serializer.data)


@api_view(["POST"])
def create_article(request):
    serializer = ArticleBaseSerializer(data=request.data)
    if serializer.is_valid():
        log(log.INFO, "Creating article by author [%s]", serializer.data["author"])
        article, error_message = create_new_article(serializer.validated_data)
        if not article:
            log(log.ERROR, "Failed to create article: %s", error_message)
            return Response({"error": error_message}, status=400)
        creation_output = ArticleGetSerializer(article)
        return Response(creation_output.data, status=201)

    log(log.ERROR, "Failed to create article")
    return Response(serializer.errors, status=400)
