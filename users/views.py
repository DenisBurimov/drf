from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_user(request):
    user = {
        "name": "Denys",
        "age": 42,
        "city": "Planet Earth",
    }
    return Response(user)
