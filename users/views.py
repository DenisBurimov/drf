from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models.user import User
from .serializers import UserSerializer, UserCreateSerializer
from users.managers.profile import UserProfileManager


@api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_user(request, phone_number: str):
    user = User.objects.get(phone_number=phone_number)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["POST"])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        user, profile = UserProfileManager().create_user_with_profile(
            phone=serializer.data["phone_number"],
            password=serializer.data["password"],
            first_name=serializer.data["first_name"],
            last_name=serializer.data["last_name"],
            description=serializer.data["description"],
        )
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
