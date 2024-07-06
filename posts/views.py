from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article


class BlogListView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "articles"

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.all()


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog-detail.html"
    context_object_name = "article"
