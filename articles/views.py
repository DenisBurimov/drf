from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models.article import Article
from .serializers import ArticleSerializer
from d3.logger import log


@api_view(["GET"])
def get_all_articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)

    log(log.INFO, "Getting [%d] articles", len(articles))
    return Response(serializer.data)
