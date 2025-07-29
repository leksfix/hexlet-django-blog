# from django.http import HttpResponse

from django.shortcuts import render


def index(request, tag=None, article_id=None):
    return render(
        request,
        "articles/index.html",
        context={
            "appname": "Hexlet-django-blog",
            "tag": tag,
            "article_id": article_id
        },
    )