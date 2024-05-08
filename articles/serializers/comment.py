from rest_framework import serializers


class CommentBaseSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    author = serializers.IntegerField(source="user_id")


class CommentAnswerSerializer(CommentBaseSerializer):
    article = serializers.IntegerField(source="article_id")
    parent_comment = serializers.IntegerField(
        source="parent_comment_id",
        required=False,
    )
