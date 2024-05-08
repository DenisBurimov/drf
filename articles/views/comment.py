from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models.article import Article
from articles.serializers import CommentBaseSerializer
from articles.managers import CommentManager


comment_manager = CommentManager()


@api_view(["post"])
def create_comment(request, uuid):
    try:
        article = Article.objects.get(uuid=uuid)
    except Article.DoesNotExist:
        return Response({"error": "Article does not exist"}, status=404)

    serializer = CommentBaseSerializer(data=request.data)
    if serializer.is_valid():
        """
        serializer.errors
        {'article': [ErrorDetail(string='A valid integer is required.', code='invalid')]}
        """
        comment = comment_manager.post_comment(article, serializer.validated_data)
        return Response(comment, status=201)
    return Response(serializer.errors, status=400)
