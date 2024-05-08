from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_articles),
    path("create", views.create_article),
    # path("update/<str:phone_number>", views.update_user),
    path("<str:uuid>", views.get_article),
]
