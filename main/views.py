from django.shortcuts import render
from django.db.models import Q
from main.apps.articles.models import Article


def dashboard(request):
    title = request.GET.get("title")
    author = request.GET.get("author")
    content = request.GET.get("content")
    articles = Article.objects.all()

    if title:
        articles = articles.filter(title__icontains=title)
    if author:
        articles = articles.filter(
            Q(author__first_name__icontains=author)
            | Q(author__last_name__icontains=author)
        )
    if content:
        articles = articles.filter(content__icontains=content)

    if request.GET.get("search"):
        template = "main/article_list.html"
    else:
        template = "main/main_info.html"
    return render(request, template, {"articles": articles})
