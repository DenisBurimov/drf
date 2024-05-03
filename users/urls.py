from django.urls import path
from . import views

urlpatterns = [
    path("get_one", views.get_user),
]
