from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_users),
    # path("create", views.create_user),
    path("create", views.UserCreate.as_view()),
    path("<str:phone_number>", views.get_user),
]
