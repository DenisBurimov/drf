from django.shortcuts import render
from articles.models import Article


def main_info(request):
    articles = Article.objects.all()
    return render(request, "d3/main_info.html", {"articles": articles})
