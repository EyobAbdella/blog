from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .forms import ArticleForm


def home(request):
    return render(request, "home.html")


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog-create.html"
    login_url = "/login"
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
