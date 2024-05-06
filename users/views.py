from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models.user import D3User
from .serializers import UserSerializer


@api_view(["GET"])
def get_all_users(request):
    users = D3User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_user(request, phone_number: str):
    user = D3User.objects.get(phone_number=phone_number)
    serializer = UserSerializer(user)
    return Response(serializer.data)


# @api_view(["POST"])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


class UserCreate(generics.CreateAPIView):
    # permission_classes = [AllowAny]
    queryset = D3User.objects.all()
    serializer_class = UserSerializer
