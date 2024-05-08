from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models.user import User
from .serializers import UserSerializer, UserProfileSerializer
from users.managers.profile import create_user_with_profile, update_user_with_profile
from d3.logger import log


@api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    log(log.INFO, "Getting [%d] users", len(users))
    return Response(serializer.data)


@api_view(["GET"])
def get_user(request, phone_number: str):
    user = User.objects.get(phone_number=phone_number)
    serializer = UserSerializer(user)

    log(log.INFO, "Getting user: [%s]", phone_number)
    return Response(serializer.data)


@api_view(["POST"])
def create_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        log(
            log.INFO,
            "User data is serialized successfully. Creating user: [%s]",
            serializer.data["phone_number"],
        )
        # serializer.save()
        user, profile = create_user_with_profile(
            phone=serializer.data["phone_number"],
            password=serializer.data["password"],
            first_name=serializer.data["first_name"],
            last_name=serializer.data["last_name"],
            description=serializer.data["description"],
        )
        assert user
        assert profile
        log(log.INFO, "User [%s] created successfully", user.phone_number)
        return Response(serializer.data, status=201)

    log(log.ERROR, "Failed to serialize user data")
    return Response(serializer.errors, status=400)


# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


@api_view(["PUT"])
def update_user(request, phone_number: str):
    user = User.objects.get(phone_number=phone_number)
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        is_updated = update_user_with_profile(
            user,
            phone=serializer.data["phone_number"],
            password=serializer.data["password"],
            first_name=serializer.data["first_name"],
            last_name=serializer.data["last_name"],
            description=serializer.data["description"],
        )
        if is_updated:
            return Response(serializer.data)
        return Response("Failed to update user", status=400)
    return Response(serializer.errors, status=400)
