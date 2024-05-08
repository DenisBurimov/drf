from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class UserProfileSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField(max_length=32, required=False)
    last_name = serializers.CharField(max_length=32, required=False)
    description = serializers.CharField(max_length=256, required=False)

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
