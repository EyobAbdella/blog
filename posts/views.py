from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm


class BlogListView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "articles"

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.all()


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog-create.html"
    login_url = "/login"
    form_class = ArticleForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog-detail.html"
    context_object_name = "article"