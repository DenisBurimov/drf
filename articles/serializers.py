from rest_framework import serializers
from users.models import Profile


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=2048)
    author = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    is_published = serializers.BooleanField()
    users_liked = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Profile.objects.all(),
    )
