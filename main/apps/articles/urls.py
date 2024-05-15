from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_articles),
    path("create", views.create_article),
    path("update/<str:uuid>", views.update_article),
    path("<str:uuid>", views.get_article),
    path("comment/<str:uuid>", views.create_comment),
]
