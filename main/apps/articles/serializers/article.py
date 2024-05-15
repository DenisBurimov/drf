from rest_framework import serializers
from main.apps.users.models import Profile


class ArticleBaseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=2048)
    author = serializers.IntegerField(source="author_id")


class ArticleGetSerializer(ArticleBaseSerializer):
    uuid = serializers.UUIDField()

    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    is_published = serializers.BooleanField()
    users_liked = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )


class ArticleUpdateSerializer(ArticleBaseSerializer):
    users_liked = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(),
        required=False,
    )
