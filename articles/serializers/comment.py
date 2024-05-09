from rest_framework import serializers


class CommentBaseSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    author = serializers.IntegerField(source="author_id")


class CommentGetSerializer(CommentBaseSerializer):
    uuid = serializers.UUIDField()
    article = serializers.IntegerField(source="article_id")
    parent_comment = serializers.IntegerField(
        source="parent_comment_id",
        required=False,
    )
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    users_liked = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )


class CommentAnswerSerializer(CommentBaseSerializer):
    article = serializers.IntegerField(source="article_id")
    parent_comment = serializers.IntegerField(
        source="parent_comment_id",
        required=False,
    )
