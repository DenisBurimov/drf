from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models.article import Article
from articles.serializers import CommentBaseSerializer


@api_view(["post"])
def create_comment(request, uuid):
    try:
        article = Article.objects.get(uuid=uuid)
    except Article.DoesNotExist:
        return Response({"error": "Article does not exist"}, status=404)

    serializer = CommentBaseSerializer(data=request.data)
    if serializer.is_valid():
        comment = serializer.save()
        return Response(comment, status=201)
    return Response(serializer.errors, status=400)
