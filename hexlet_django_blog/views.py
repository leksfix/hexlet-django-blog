from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView

'''
def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World",
        },
    )
'''

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World (class)"
        return context
    
    def get(self, request, *args, **kwargs):
        return redirect(reverse('articles_index', kwargs={'tag': 'python', 'article_id': 42}))


def about(request):
    return render(request, "about.html")