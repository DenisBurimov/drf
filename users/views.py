from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models.user import D3User
from .serializers import UserSerializer


@api_view(["GET"])
def get_user(request, phone_number: str):
    user = D3User.objects.get(phone_number=phone_number)
    serializer = UserSerializer(user)
    return Response(serializer.data)
