from django.shortcuts import render
from articles.models import Article


def main_info(request):
    articles = Article.objects.all()
    return render(request, "main/main_info.html", {"articles": articles})
