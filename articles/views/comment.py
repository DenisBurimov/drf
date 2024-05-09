from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models.article import Article
from articles.serializers import CommentBaseSerializer, CommentGetSerializer
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
        comment, error_message = comment_manager.post_comment(
            article, serializer.validated_data
        )
        if not comment:
            return Response({"error": error_message}, status=400)
        comment_output = CommentGetSerializer(comment)
        return Response(comment_output.data, status=201)
    return Response(serializer.errors, status=400)
