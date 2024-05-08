from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_articles),
    # path("create", views.create_user),
    # path("update/<str:phone_number>", views.update_user),
    # path("<str:phone_number>", views.get_user),
]
