# from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(
        request,
        "articles/index.html",
        context={
            "appname": "Hexlet-django-blog",
        },
    )