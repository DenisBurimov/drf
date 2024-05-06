from rest_framework import serializers
from .models import D3User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = D3User
        fields = ["id", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}
