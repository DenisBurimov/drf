from django.urls import path
from . import views

urlpatterns = [
    path("<str:phone_number>", views.get_user),
]
