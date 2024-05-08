from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    content = serializers.CharField(max_length=2048)
    author = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    is_published = serializers.BooleanField()
    users_liked = serializers.ListField(child=serializers.IntegerField())
