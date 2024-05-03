from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def main_info(request):
    person = {
        "name": "John",
        "age": 30,
        "city": "New York",
    }
    return Response(person)
